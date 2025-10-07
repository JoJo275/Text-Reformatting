#!/usr/bin/env python3
"""
short_lines.py

A program that takes two command line arguments: an input file name
and an output file name. The program reads the input file containing
short lines (< 30 chars) and outputs text reformatted into lines
of 30 characters (including spaces and punctuation).

Errors handled:
- Missing arguments
- Input file not found
- Input file empty
- File read/write errors
- Unsupported file types
"""

import sys
import os

ACCEPTED_FILE_FORMATS = (".csv", ".txt", ".docx", ".pdf", ".md", ".json", ".text")


def validate_args():
    """Check command-line arguments."""
    if len(sys.argv) != 3:
        sys.exit("Usage: python short_lines.py <input_file> <output_file>")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.isfile(input_filename):
        sys.exit(f"Error: Input file does not exist: {input_filename}")

    if not input_filename.endswith(ACCEPTED_FILE_FORMATS) or not output_filename.endswith(ACCEPTED_FILE_FORMATS):
        sys.exit(
            "Error: Both input and output files must have a valid extension:\n"
            ".csv .txt .docx .pdf .md .json .text"
        )

    return input_filename, output_filename


def read_input_file(filename):
    """Read all lines from file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except Exception as e:
        sys.exit(f"Error reading input file: {e}")

    if not content:
        sys.exit(f"Error: Input file is empty: {filename}")

    return content


def reformat_text(content, line_length=30):
    """Reformat text into 30-character lines."""
    try:
        # Remove extra whitespace and line breaks
        text = " ".join(content.split())
        # Break into chunks of 30 chars
        lines = [text[i:i + line_length] for i in range(0, len(text), line_length)]
        return "\n".join(lines)
    except Exception as e:
        sys.exit(f"Error reformatting text: {e}")


def write_output_file(filename, text):
    """Write reformatted text to output file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        sys.exit(f"Error writing output file: {e}")


def main():
    input_filename, output_filename = validate_args()
    content = read_input_file(input_filename)
    new_text = reformat_text(content)
    write_output_file(output_filename, new_text)
    print(f"Successfully wrote reformatted text to: {output_filename}")


if __name__ == "__main__":
    main()
