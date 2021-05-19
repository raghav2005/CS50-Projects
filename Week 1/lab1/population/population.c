#include <cs50.h>
#include <stdio.h>

// define functions
int get_size(int lowest, string display_str);
int calculate(int start, int end);

int main(void)
{
    // get start size
    int start_size = get_size(9, "Start size: ");

    // get end size
    int end_size = get_size(start_size, "End size: ");

    // calculate number of years until we reach threshold
    int no_of_years = calculate(start_size, end_size);

    // print number of years
    printf("Years: %i\n", no_of_years);
}

// ask for starting size
int get_size(int lowest, string display_str)
{
    int n;

    // can't have less than lowest entered
    do
    {
        n = get_int("%s", display_str);
    }
    while (n < lowest);

    return n;
}

// calculate number of years
int calculate(int start, int end)
{
    int years = 0;

    while (end > start)
    {
        // calculate new births + deaths
        int born = start / 3;
        int dead = start / 4;

        // new population size
        start += born;
        start -= dead;

        // add to no. of years passed
        years++;
    }

    return years;
}