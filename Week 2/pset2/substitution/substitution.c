#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// prototypes
bool validate_key(string key);
bool no_repeats(string key);
bool all_alpha(string key);
string encrypt(string key, string plaintext);

int main(int argc, string argv[])
{
    // should only have 1 command-line argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    bool valid_key = validate_key(argv[1]);

    // command-line argument should be all letters in the alphabet
    if (valid_key == false)
    {
        printf("Key must to be 26 unique alphabets\n");
        return 1;
    }

    string plaintext = get_string("plaintext: ");
    string ciphertext = encrypt(argv[1], plaintext);

    printf("ciphertext: %s\n", ciphertext);
    return 0;
}

bool validate_key(string key)
{
    // needs to be 26 characters long
    if (strlen(key) != 26)
    {
        return false;
    }

    // all characters must be alphabetical characters
    bool chars_valid = all_alpha(key);

    // check if all 26 letters in the alphabet are in the string
    bool has_no_repeats = no_repeats(key);

    if (chars_valid == false || has_no_repeats == false)
    {
        return false;
    }
    else
    {
        return true;
    }
}

bool all_alpha(string key)
{
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (isalpha(key[i]) == 0)
        {
            return false;
        }
    }

    return true;
}

bool no_repeats(string key)
{
    // empty array to hold each character when iterating through key
    char chars_in_key[26];

    // iterate through key
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        // iterate through chars_in_key
        for (int y = 0; y < 26; y++)
        {
            // check if any characters have already been entered into the array
            if (chars_in_key[y] == key[i])
            {
                return false;
            }
        }

        chars_in_key[i] = key[i];
    }

    return true;
}

string encrypt(string key, string plaintext)
{
    string ciphertext = plaintext;

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // check if needs to be converted
        if (isalpha(plaintext[i]) != 0)
        {
            // if lower case
            if (islower(plaintext[i]) != 0)
            {
                // a = 97, z = 122, so - 97 to find index in key
                ciphertext[i] = tolower(key[plaintext[i] - 97]);
            }
            else
            {
                // A = 65, Z = 90, so - 65 to find index in key
                ciphertext[i] = toupper(key[plaintext[i] - 65]);
            }
        }

        ciphertext[i] = plaintext[i];
    }

    return ciphertext;
}