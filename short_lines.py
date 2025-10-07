"""short_lines.py

Implement of program that takes two command line arguments: an input file name
and an output file name.
The input and output file type can be of any type
The program reads the input file, which contains multiple short lines of text:
lines of text shorter than 30 characters including spaces and punctiuation.
The program then takes that input file and in a new output file specified at
the command line by the user, outputs lines a text with 30 characters per line
including spaces and punctuation.


The program should print an error message and exit gracefully if:

- If input file is not found
- if the input file is empty
- if there was an error reading input file
- if the program has an error reformatting the input file
- if the input and output file types are not supported
- if three arguments are not provided

"""

# !/usr/bin/env python3

# TODO

# [ ]Implement a program that takes one file and reformats it as another
# file with text per line at least 30 characters including spaces and
# punctuation.
# [ ]Check output file against expected output
# [ ]Test program with all errors listed in docstring at the beginning of the 
# document.
# [ ](NOT SURE)Implement test_short_lines.py to test short_lines.py?


import sys
import os

ACCEPTED_FILE_FORMATS = ".csv .txt .docx .pdf .md .json .text"


def main():

    def get_input_file():
        if len(sys.argv) != 3:
            sys.exit("Usage: python pizza.py <filename.csv>")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.isfile(input_filename):
        sys.exit(f"Input file does not exist: {input_filename}")

    if not input_filename.endswith(ACCEPTED_FILE_FORMATS) or not output_filename.endswith(ACCEPTED_FILE_FORMATS):
        sys.exit("Both input and output files must have a valid extension: "
                 ".csv .txt .docx .pdf .md .json .text")

    def open_input_file():
        try:
            with open(input_filename, "r", encoding="utf-8") as infile:
                lines = infile.readlines()
                rows = list(lines)
        except Exception as e:
            sys.exit(f"Error reading {input_filename}: {e}")
        if not rows:
            sys.exit(f"Input file is empty: {input_filename}")


if __name__ == "__main__":
    main()

"""short_lines.py"""
