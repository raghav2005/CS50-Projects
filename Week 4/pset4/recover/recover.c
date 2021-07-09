#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// define prototypes
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // only 1 argument allowed
    if (argc != 2)
    {
        printf("Usage: ./recover image_file\n");
        return 1;
    }

    // open image_file
    char *inp_file_name = argv[1];
    FILE *inp_file_pointer = fopen(inp_file_name, "r");

    // must be a valid file
    if (inp_file_pointer == NULL)
    {
        printf("Couldn't open file: %s", inp_file_name);
        return 1;
    }

    // init necessary vars
    BYTE buffer[512];
    int count_img = 0;
    FILE *out_file_pointer = NULL;
    char out_file_name[8];

    // repeat until end of card.raw
    while (fread(&buffer, 512, 1, inp_file_pointer) != 0)
    {
        // check start of new jpeg (0xff 0xd8 0xff 0xe*)
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // close prev if not 1st jpeg
            if (!(count_img == 0))
            {
                fclose(out_file_pointer);
            }

            // write jpeg into file name in form: 001.jpg, 002.jpg etc.
            sprintf(out_file_name, "%03i.jpg", count_img);

            // open out_file to write to
            out_file_pointer = fopen(out_file_name, "w");

            // count number of images found
            count_img += 1;
        }

        // write to file if jpeg has been found
        if (!(count_img == 0))
        {
            fwrite(&buffer, 512, 1, out_file_pointer);
        }
    }

    // close all files
    fclose(inp_file_pointer);
    fclose(out_file_pointer);

    return 0;
}