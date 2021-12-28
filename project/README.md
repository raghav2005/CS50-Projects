=======================

# CONVERTERS

## REQUIREMENTS

### PYTHON LIBS ON TERMINAL

Dependencies are in `requirements.txt`

1. To install the dependencies, first go to converters directory, once in,

- ON MAC run:
```
$ pip3 install -r requirements.txt
```
- ON WINDOWS run:
```
$ pip install -r requirements.txt
```

2. Afterwards, you can run the python file `main.py` with,

- ON MAC:
```
$ python3 main.py
```
* or
```
$ python main.py
```
depending on whatever python 3 is called on Terminal

- ON WINDOWS:
```
$ python main.py
```

### PYTHON FILE FOR API

In order to use the conversion API, you must first create a file called with
the filename `APIs.py`.

Once you have done this, visit https://fixer.io/ and sign up with a free plan,
following the instructions to get the API.

Once you have the api, open `APIs.py` and enter the following code, with 
YOURAPI replaced with the actual API as a string:

```python
fixer_API = YOURAPI

```

e.g.

```python
fixer_API = 'blahblahblahblahblahblahblahblahblah'

```