# all libs
import csv
import re
import sys


def main():

    check_args()
    most_likely()

    return


# only 3 command-line arguments not including python
def check_args():

    if len(sys.argv) != 3:

        print('Usage: python dna.py data.csv sequence.txt')

        # like return 1 in C
        sys.exit(1)

    else:
        return


# output most likely match
def most_likely():

    # read csv file into memory
    csv_filename = sys.argv[1]
    csv_file = open(csv_filename, newline='')

    db_reader = csv.reader(csv_file, delimiter=',', quotechar='|')

    for x, row in enumerate(db_reader):

        if x == 0:

            # read txt file into memory
            txt_filename = sys.argv[2]
            txt_file = open(txt_filename, 'r')

            txt_line = next(txt_file)
            longest_strs = []

            for x in range(1, len(row)):

                sequence = row[x]
                # get all matches
                matches = (match[0] for match in re.finditer(fr'(?:{sequence})+', txt_line))

                # incase of error
                try:
                    longest = int(len(max(matches, key=len)) / len(sequence))
                    longest_strs.append(longest)
                except ValueError:
                    longest_strs.append(0)

        else:

            list_db_strs = list(map(int, row[1:]))

            if list_db_strs == longest_strs:
                print(row[0])
                # exit loop
                break

    else:
        print('No match')

    csv_file.close()

    return


if __name__ == '__main__':
    main()