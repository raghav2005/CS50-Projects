def main():

    # forever loop
    while True:

        # has to be int 1 - 8 inclusive
        try:
            height = int(input('Height: '))

            if height >= 1 and height <= 8:
                break

        except ValueError:
            pass

    display_height(height, height)


def display_height(height, n):

    # base-case
    if height == 0:
        return

    # recursion
    display_height(height - 1, n)

    # display all
    print(' ' * (n - height), end='')
    print('#' * height, end='')
    print('  ', end='')
    print('#' * height)


if __name__ == '__main__':
    main()
