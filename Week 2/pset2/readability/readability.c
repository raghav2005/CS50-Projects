#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// prototypes
int calculate(string text);
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
float value_per_100_words(int value, int words);

int main(void)
{
    string text = get_string("Text: ");
    int level = calculate(text);

    if (level >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (level < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", level);
    }
}

int calculate(string text)
{
    // values needed from text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // calculations from values
    float L = value_per_100_words(letters, words);
    float S = value_per_100_words(sentences, words);

    float index = 0.0588 * L - 0.296 * S - 15.8;

    return round(index);
}

int count_letters(string text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // if a letter
        if (isalpha(text[i]) != 0)
        {
            count += 1;
        }
    }
    // only alphabets counted
    return count;
}

int count_words(string text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // if a space
        if (text[i] == ' ')
        {
            count += 1;
        }
    }

    // there are always space + 1 words
    return count + 1;
}

int count_sentences(string text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // if the end of a sentence
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count += 1;
        }
    }

    // can assume Mr. X. is counted as 2 sentences
    return count;
}

// same calculation for letters and sentences
float value_per_100_words(int value, int words)
{
    // round to approx 2 d.p. - might get extra values after
    return round((value / (float)words) * 100 * 100.0) / 100.0;
}