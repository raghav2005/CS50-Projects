// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

int dictionary_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // get hash value by hashing word
    int hash_value = hash(word);

    // access linked list at that index in the hash table
    node *n = table[hash_value];

    // go through linked list
    while (n != NULL)
    {
        // check if the word matches
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }

        // pointer to next node
        n = n->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;

    while ((c = tolower(*word++)))
    {
        // hash * 33 + c
        hash = ((hash << 5) + hash) + c;
    }

    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // open dictionary file
    FILE *dictionary_pointer = fopen(dictionary, "r");

    if (dictionary_pointer == NULL)
    {
        printf("Cannot open %s\n", dictionary);
        return false;
    }

    // word array
    char next_word[LENGTH + 1];

    // read file 1 string at a time
    while (fscanf(dictionary_pointer, "%s", next_word) != EOF)
    {
        // new node for each word
        node *new_node = malloc(sizeof(node));

        if (new_node == NULL)
        {
            return false;
        }

        // copy word into new_node
        strcpy(new_node->word, next_word);

        // get hash value by hashing the word
        int hash_value = hash(next_word);

        // put new_node into hash table at that location
        new_node->next = table[hash_value];
        table[hash_value] = new_node;

        dictionary_size += 1;
    }

    // close file
    fclose(dictionary_pointer);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dictionary_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // go through buckets
    for (int i = 0; i < N; i++)
    {
        // assign cursor
        node *n = table[i];

        // loop through linked list
        while (n != NULL)
        {
            node *tmp = n;
            n = n->next;
            free(tmp);
        }

        // if cursor is null
        if (n == NULL && i == N - 1)
        {
            return true;
        }
    }

    return false;
}
