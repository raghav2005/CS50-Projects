def main():

    card_number = get_card_number()
    checksum = calculate_checksum(card_number)
    validate_type(card_number, checksum)


def get_card_number():

    while True:

        # must be an int
        number = input('Number: ')

        if number.isnumeric():
            break

    return number


def calculate_checksum(number):

    sum_evens = 0
    sum_odds = 0

    number = reversed([int(i) for i in number])

    # refer to credit from week 1
    for x, y in enumerate(number):

        if (x + 1) % 2 == 0:

            odd_digit = y * 2

            if odd_digit > 9:
                sum_odds += int(odd_digit / 10) + odd_digit % 10
            else:
                sum_odds += odd_digit

        else:
            sum_evens += y

    total = sum_evens + sum_odds

    return total


def validate_type(number, checksum):

    start_number = int(number[:2])
    card_length = len(number)
    checksum_last_digit = checksum % 10

    # print solution
    if checksum_last_digit == 0:
        if (start_number == 34 or start_number == 37) and card_length == 15:
            print('AMEX')
        elif (int(number[0]) == 4) and (card_length == 13 or card_length == 16):
            print('VISA')
        elif (start_number in range(51, 56)) and card_length == 16:
            print('MASTERCARD')
        else:
            print('INVALID')
    else:
        print('INVALID')


if __name__ == '__main__':
    main()
