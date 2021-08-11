-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get description from known info
SELECT description FROM crime_scene_reports WHERE year = '2020' AND month = '7' AND day = '28' AND street = 'Chamberlin Street';

-- Get activity description of the 3 witnesses
SELECT transcript FROM interviews WHERE year = '2020' AND month = '7' AND day = '28' AND transcript LIKE '%courthouse%';

-- Get names from license plates exiting the courthouse within 10 minutes of the theft;
SELECT DISTINCT(name) FROM
    people JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = '2020' AND month = '7' AND day = '28' AND hour = '10' AND minute >= '15' AND minute <= '25' AND activity = 'exit';

-- Get names from people who withdrew money from ATM on Fifer Street that day
SELECT DISTINCT(name) FROM
    people JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = '2020' AND month = '7' AND day = '28' AND transaction_type = 'withdraw' AND atm_location = 'Fifer Street';

-- Get names of people who took the earliest flight out of FiftyVille the next day
SELECT DISTINCT(name) FROM
    people JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (SELECT id FROM flights WHERE year = '2020' AND month = '7' AND day = '29' ORDER BY hour, minute LIMIT 1);

-- Get names of people who made a call lasting less than 1 minute (60 seconds) on that day
SELECT DISTINCT(name) FROM
    people JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = '2020' AND month = '7' AND day = '28' AND duration < '60';

-- Find name that's common from all 4 previous queries
SELECT DISTINCT(name) FROM
    people JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = '2020' AND month = '7' AND day = '28' AND hour = '10' AND minute >= '15' AND minute <= '25' AND activity = 'exit'
INTERSECT
SELECT DISTINCT(name) FROM
    people JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = '2020' AND month = '7' AND day = '28' AND transaction_type = 'withdraw' AND atm_location = 'Fifer Street'
INTERSECT
SELECT DISTINCT(name) FROM
    people JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (SELECT id FROM flights WHERE year = '2020' AND month = '7' AND day = '29' ORDER BY hour, minute LIMIT 1)
INTERSECT
SELECT DISTINCT(name) FROM
    people JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = '2020' AND month = '7' AND day = '28' AND duration < '60';

-- Get destination
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE year = '2020' AND month = '7' AND day = '29' ORDER BY hour, minute LIMIT 1);

-- Get accomplice
SELECT name FROM
    people JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE year = '2020' AND month = '7' AND day = '28' AND duration < '60' AND caller = (SELECT phone_number FROM people WHERE name = 'Ernest');
