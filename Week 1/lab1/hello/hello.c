#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get name
    string name = get_string("What is your name?: ");
    // output name
    printf("hello, %s\n", name);
}