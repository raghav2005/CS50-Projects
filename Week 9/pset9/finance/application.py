import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_cash = db.execute("SELECT * FROM users WHERE id = ?;", session["user_id"])
    cash_owned = user_cash[0]["cash"]
    user_stocks = db.execute(
        "SELECT company, symbol, SUM(shares) as sum_shares FROM transactions WHERE user_id = ? GROUP BY user_id, company, symbol HAVING sum_shares > 0;", session["user_id"])

    total_sum = 0

    user_stocks = [dict(stock, **{"price": lookup(stock["symbol"])["price"]}) for stock in user_stocks]
    user_stocks = [dict(stock, **{"total": stock["price"] * stock["sum_shares"]}) for stock in user_stocks]

    total_sum = cash_owned + sum([stock["total"] for stock in user_stocks])

    return render_template("index.html", cash_owned=cash_owned, user_stocks=user_stocks, total_sum=total_sum)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        query = lookup(symbol)

        if not symbol:
            return apology("Missing symbol")

        if not shares:
            return apology("Missing shares")

        try:
            shares = int(shares)
        except ValueError:
            return apology("Invalid shares - must be INT")

        if shares <= 0:
            return apology("Invalid shares - must be > 0")

        if not query:
            return apology("Invalid symbol")

        user_cash = db.execute("SELECT * FROM users WHERE id = ?;", session["user_id"])
        cash_owned = user_cash[0]["cash"]
        total_prices = query["price"] * shares

        if cash_owned < total_prices:
            return apology("Insufficient cash")

        db.execute("INSERT INTO transactions(user_id, company, symbol, shares, price) VALUES (?, ?, ?, ?, ?);",
                    session["user_id"], query["name"], symbol, shares, query["price"])
        db.execute("UPDATE users SET cash = ? WHERE id = ?;", (cash_owned - total_prices), session["user_id"])

        flash("Transaction successful!")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?;", session["user_id"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        query = lookup(request.form.get("symbol"))

        if not query:
            return apology("Invalid symbol")

        return render_template("quote.html", query=query)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Missing username")

        if not password:
            return apology("Missing password")

        if not confirmation:
            return apology("Password doesn't match")

        rows = db.execute("SELECT * FROM users WHERE username = ?;", username)

        if len(rows) != 0:
            return apology(f"The username '{username}' already exists. Please choose another name.")

        if password != confirmation:
            return apology("Password doesn't match")

        curr_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", username, generate_password_hash(password))

        session["user_id"] = curr_id

        flash("Registered!")

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    symbols_owned = db.execute(
        "SELECT symbol, SUM(shares) as sum_shares FROM transactions WHERE user_id = ? GROUP by user_id, symbol HAVING sum_shares > 0;", session["user_id"])

    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        query = lookup(symbol)

        if not symbol:
            return apology("Missing symbol")

        if not shares:
            return apology("Missing shares")

        try:
            shares = int(shares)
        except ValueError:
            return apology("Invalid shares - must be INT")

        if shares <= 0:
            return apology("Invalid shares - must be > 0")

        symbols_dict = {symbol_owned["symbol"]: symbol_owned["sum_shares"] for symbol_owned in symbols_owned}

        if symbols_dict[symbol] < shares:
            return apology("Too many shares")

        user_cash = db.execute("SELECT * FROM users WHERE id = ?;", session["user_id"])
        cash_owned = user_cash[0]["cash"]

        db.execute("INSERT INTO transactions(user_id, company, symbol, shares, price) VALUES (?, ?, ?, ?, ?)",
                    session["user_id"], query["name"], symbol, -shares, query["price"])
        db.execute("UPDATE users SET cash = ? WHERE id = ?;", (cash_owned + (query["price"] * shares)), session["user_id"])

        flash("Sold!")

        return redirect("/")

    else:
        return render_template("sell.html", symbols=symbols_owned)


@app.route("/reset", methods=["GET", "POST"])
@login_required
def reset():

    if request.method == "POST":

        password = request.form.get("password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        if not password:
            return apology("Missing old password")

        rows = db.execute("SELECT * FROM users WHERE id = ?;", session["user_id"])

        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid password")

        if not new_password:
            return apology("Missing new password")

        if not confirmation:
            return apology("Password doesn't match")

        db.execute("UPDATE users SET hash = ? WHERE id = ?;", generate_password_hash(new_password), session["user_id"])

        flash("Password reset successful!")

        return redirect("/")

    else:
        return render_template("reset.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
