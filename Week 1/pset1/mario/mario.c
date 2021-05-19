#include <cs50.h>
#include <stdio.h>

// define functions
void display_pyramids(int height);

int main(void)
{
    // ask for input between 1 and 8, inclusive
    int height;

    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // display (height) no. of pygramids
    display_pyramids(height);
}

// display all pyramids
void display_pyramids(int height)
{
    // j loops to be the number of rows required (height)
    for (int j = 1; j <= height; j++)
    {
        // FIRST HALF
        // number of spaces before #s begin in this row
        for (int i = height; i > j; i--)
        {
            printf(" ");
        }
        // remaining number of places in the row to be filled with #s
        for (int i = 0; i < j; i++)
        {
            printf("#");
        }

        // 2 SPACES BREAK
        printf("  ");

        // SECOND HALF
        for (int i = 0; i < j; i++)
        {
            printf("#");
        }

        // NEXT ROW
        printf("\n");
    }
}