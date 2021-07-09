#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop through the rows
    for (int i = 0; i < height; i++)
    {
        // loop through the columns
        for (int j = 0; j < width; j++)
        {
            // get RGBTRIPLE values
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            // calculate average
            int average = round((red + green + blue) / 3);

            // set r, g, and b values to average
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // loop through the rows
    for (int i = 0; i < height; i++)
    {
        // loop through the columns
        for (int j = 0; j < width; j++)
        {
            // get RGBTRIPLE values
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // calculate sepia values
            int sepia_red = round(0.393 * red + 0.769 * green + 0.189 * blue);
            int sepia_green = round(0.349 * red + 0.686 * green + 0.168 * blue);
            int sepia_blue = round(0.272 * red + 0.534 * green + 0.131 * blue);

            int sepia_rgb[] = {sepia_red, sepia_green, sepia_blue};

            // set to 255 if over
            for (int z = 0, n = 3; z < n; z++)
            {
                if (sepia_rgb[z] > 255)
                {
                    sepia_rgb[z] = 255;
                }
            }

            // reassign values
            image[i][j].rgbtRed = sepia_rgb[0];
            image[i][j].rgbtGreen = sepia_rgb[1];
            image[i][j].rgbtBlue = sepia_rgb[2];
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // loop through the rows
    for (int i = 0; i < height; i++)
    {
        // loop through half of the columns
        for (int j = 0; j < (width / 2); j++)
        {
            // get temporary RGBTRIPLE values
            int temp_red = image[i][j].rgbtRed;
            int temp_green = image[i][j].rgbtGreen;
            int temp_blue = image[i][j].rgbtBlue;

            // assign values of the pixel reflected vertically down the middle to current pixel
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;

            // assign temporary values of the pixel to the pixel reflected
            image[i][width - j - 1].rgbtRed = temp_red;
            image[i][width - j - 1].rgbtGreen = temp_green;
            image[i][width - j - 1].rgbtBlue = temp_blue;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // create a temporary image which holds blurred values
    RGBTRIPLE temp_img[height][width];

    // loop through the rows
    for (int i = 0; i < height; i++)
    {
        // loop through the columns
        for (int j = 0; j < width; j++)
        {
            // required values
            int total_red = 0;
            int total_green = 0;
            int total_blue = 0;
            float neighbour_count = 0.00;

            // get neighbour pixels
            for (int x = 0; x < 3; x++)
            {
                for (int y = 0; y < 3; y++)
                {
                    // get currently working on pixel
                    int curr_x = i + x - 1;
                    int curr_y = j + y - 1;

                    // validate neighbouring pixels
                    if (curr_x < 0 || curr_y < 0 || curr_x > (height - 1) || curr_y > (width - 1))
                    {
                        continue;
                    }

                    // get rgb values
                    total_red += image[curr_x][curr_y].rgbtRed;
                    total_green += image[curr_x][curr_y].rgbtGreen;
                    total_blue += image[curr_x][curr_y].rgbtBlue;

                    neighbour_count += 1.00;
                }

                // get average of neighbouring pixels
                temp_img[i][j].rgbtRed = round(total_red / neighbour_count);
                temp_img[i][j].rgbtGreen = round(total_green / neighbour_count);
                temp_img[i][j].rgbtBlue = round(total_blue / neighbour_count);
            }
        }
    }

    // loop through the rows
    for (int i = 0; i < height; i++)
    {
        // loop through the columns
        for (int j = 0; j < width; j++)
        {
            // copy the temporary blurred image to the original image
            image[i][j].rgbtRed = temp_img[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp_img[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp_img[i][j].rgbtBlue;
        }
    }

    return;
}
