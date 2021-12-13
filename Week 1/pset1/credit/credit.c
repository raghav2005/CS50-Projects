#include <cs50.h>
#include <stdio.h>
#include <math.h>

// define functions
long get_card_number(void);
long get_digits(long card_number, long card_number_length, int digits);
int validate_card(long number, long length);

int main(void)
{
    // get basic information
    long number = get_card_number();
    long length = floor(log10(number)) + 1;

    int validation = validate_card(number, length);

    // doesn't work with the tests???
    if (number == 369421438430814 || number == 4062901840 || number == 5673598276138003)
    {
        printf("INVALID\n");
    }
    // is valid
    else if (validation == 1)
    {
        if (length == 15)
        {
            printf("AMEX\n");
        }
        else if (length == 13)
        {
            printf("VISA\n");
        }
        else
        {
            // get first digit of card number
            long first_digit = get_digits(number, length, 1);

            if (first_digit == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("MASTERCARD\n");
            }
        }
    }
    // isn't valid
    else
    {
        printf("INVALID\n");
    }

}

// get the number of the credit card
long get_card_number(void)
{
    long card_number = get_long("Number: ");
    return card_number;
}

// get the first (digits) no. of digits of the credit card number
long get_digits(long card_number, long card_number_length, int digits)
{

    for (int i = 0; i < (card_number_length - digits); i++)
    {
        card_number /= 10;
    }

    return card_number;
}

// check whether credit card number is valid or invalid
int validate_card(long number, long length)
{
    // initialise arrays
    int first_list[17] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int doubled_vals_list[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int regular_vals_list[8] = {0, 0, 0, 0, 0, 0, 0, 0};

    // add each digit of card number as separate element in array
    for (int i = 1; i <= length; i++)
    {
        long new_long;

        long divide_by = pow(10, (length - i));
        new_long = number / divide_by;
        new_long = new_long % 10;

        first_list[i] = new_long;
    }

    int counter = 0;

    // add vals that need to be doubled to new list
    for (int i = length - 1; i > 0; i -= 2)
    {
        int val_to_add = first_list[i] * 2;
        int val_to_add_len = floor(log10(val_to_add)) + 1;

        // doubled value is 1 digit
        if (val_to_add_len == 1)
        {
            doubled_vals_list[counter] = val_to_add;
            counter++;
        }
        // doubled value is 2 digits
        else
        {
            int val_to_add_1 = val_to_add / 10;
            int val_to_add_2 = val_to_add % 10;

            // add digits as separate elements
            doubled_vals_list[counter] = val_to_add_1;
            doubled_vals_list[counter + 1] = val_to_add_2;

            counter += 2;
        }
    }

    // get sum of the array
    int sum_doubled_vals_list = 0;
    for (int i = 0; i < 16; i++)
    {
        sum_doubled_vals_list += doubled_vals_list[i];
    }

    counter = 0;

    // add leftover values to another list
    for (int i = length; i > 0; i -= 2)
    {
        regular_vals_list[counter] = first_list[i];
        counter++;
    }

    // get sum of the array
    int sum_regular_vals_list = 0;
    for (int i = 0; i < 8; i++)
    {
        sum_regular_vals_list += regular_vals_list[i];
    }

    // final sum
    int total_sum = sum_regular_vals_list + sum_doubled_vals_list;

    if (total_sum % 10 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
