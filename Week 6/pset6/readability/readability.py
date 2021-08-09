# all libs
import cs50
import re
import string


def main():

    # get text
    user_text = cs50.get_string('Text: ')

    # basic ints
    letters = len(re.findall('[a-zA-Z]', user_text))
    words = len(user_text.split())
    sentences = len(re.findall(r'[.!?]+', user_text))

    grade = get_grade(letters, words, sentences)

    output_grade(grade)


def get_grade(letters, words, sentences):

    # get values
    words_per_100 = words / 100
    l = letters / words_per_100
    s = sentences / words_per_100

    # actual calculation
    return round(0.0588 * l - 0.296 * s - 15.8)


def output_grade(grade):

    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print("Grade", grade)


if __name__ == '__main__':
    main()