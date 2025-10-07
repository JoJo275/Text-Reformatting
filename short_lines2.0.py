#!/usr/bin/env python3
"""
short_lines.py

A program that takes two or three command line arguments:
1. Input file name
2. Output file name
3. (Optional) Number of characters per line

The program reads an input file containing short lines (< 30 chars)
and outputs reformatted text with a fixed number of characters per line.

If no line length is provided, the user will be prompted to enter one.

Errors handled:
- Missing arguments
- Input file not found
- Input file empty
- Invalid or unsupported file types
- Invalid line length input
- File read/write errors
"""

import sys
import os

ACCEPTED_FILE_FORMATS = (".csv", ".txt", ".docx", ".pdf", ".md", ".json", ".text")


def validate_args():
    """Validate command-line arguments and file names."""
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        sys.exit("Usage: python short_lines.py <input_file> <output_file> [line_length]")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check file existence
    if not os.path.isfile(input_filename):
        sys.exit(f"Error: Input file does not exist: {input_filename}")

    # Check file types
    if not input_filename.endswith(ACCEPTED_FILE_FORMATS) or not output_filename.endswith(ACCEPTED_FILE_FORMATS):
        sys.exit(
            "Error: Both input and output files must have a valid extension:\n"
            ".csv .txt .docx .pdf .md .json .text"
        )

    # Optional line length argument
    if len(sys.argv) == 4:
        try:
            line_length = int(sys.argv[3])
            if line_length <= 0:
                sys.exit("Error: Line length must be a positive integer greater than zero.")
        except ValueError:
            sys.exit("Error: Line length must be a valid integer.")
    else:
        line_length = None

    return input_filename, output_filename, line_length


def get_line_length(default=77):
    """Prompt the user for line length with error checking."""
    while True:
        try:
            user_input = input(f"How many characters per line would you like (default {default}): ").strip()
            if user_input == "":
                return default
            length = int(user_input)
            if length <= 0:
                print("Please enter a positive number greater than 0.")
                continue
            return length
        except ValueError:
            print('Please enter a valid number (e.g., 1, 19, 234).')


def read_input_file(filename):
    """Read all content from the input file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except Exception as e:
        sys.exit(f"Error reading input file: {e}")

    if not content:
        sys.exit(f"Error: Input file is empty: {filename}")

    return content


def reformat_text(content, line_length):
    """Reformat text into fixed-length lines."""
    try:
        text = " ".join(content.split())  # Collapse extra spaces/newlines
        lines = [text[i:i + line_length] for i in range(0, len(text), line_length)]
        return "\n".join(lines)
    except Exception as e:
        sys.exit(f"Error reformatting text: {e}")


def write_output_file(filename, text):
    """Write reformatted text to the output file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        sys.exit(f"Error writing output file: {e}")


def main():
    """Main program logic."""
    input_filename, output_filename, line_length = validate_args()

    # Ask user interactively if not provided as argument
    if line_length is None:
        line_length = get_line_length(default=77)

    content = read_input_file(input_filename)
    new_text = reformat_text(content, line_length)
    write_output_file(output_filename, new_text)

    print(f"\n✅ Successfully wrote reformatted text to: {output_filename}")
    print(f"   Each line is {line_length} characters long.")


if __name__ == "__main__":
    main()
