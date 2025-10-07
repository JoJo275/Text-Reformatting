#!/usr/bin/env python3
"""
short_lines.py

A program that takes two to four command line arguments:
1. Input file name
2. Output file name
3. (Optional) Number of characters per line
4. (Optional) Number of sentences per paragraph

The program reads an input file containing short lines and outputs
text reformatted into paragraphs where:
- Lines break only between whole words
- Sentences are grouped into user-defined paragraphs
- Paragraphs are separated by blank lines

Errors handled:
- Missing arguments
- Input file not found
- Input file empty
- Invalid or unsupported file types
- Invalid numeric arguments
- File read/write errors
"""

import sys
import os
import textwrap
import re

ACCEPTED_FILE_FORMATS = (".csv", ".txt", ".docx", ".pdf", ".md", ".json", ".text")


# -----------------------------
# ARGUMENT VALIDATION
# -----------------------------
def validate_args():
    """Validate command-line arguments and file names."""
    if len(sys.argv) < 3 or len(sys.argv) > 5:
        sys.exit("Usage: python short_lines.py <input_file> <output_file> [line_length] [sentences_per_paragraph]")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # File existence check
    if not os.path.isfile(input_filename):
        sys.exit(f"Error: Input file does not exist: {input_filename}")

    # File type validation
    if not input_filename.endswith(ACCEPTED_FILE_FORMATS) or not output_filename.endswith(ACCEPTED_FILE_FORMATS):
        sys.exit(
            "Error: Both input and output files must have a valid extension:\n"
            ".csv .txt .docx .pdf .md .json .text"
        )

    # Optional arguments
    line_length = None
    sentences_per_paragraph = None

    if len(sys.argv) >= 4:
        try:
            line_length = int(sys.argv[3])
            if line_length <= 0:
                sys.exit("Error: Line length must be a positive integer greater than zero.")
        except ValueError:
            sys.exit("Error: Line length must be a valid integer.")

    if len(sys.argv) == 5:
        try:
            sentences_per_paragraph = int(sys.argv[4])
            if sentences_per_paragraph <= 0:
                sys.exit("Error: Sentences per paragraph must be greater than zero.")
        except ValueError:
            sys.exit("Error: Sentences per paragraph must be a valid integer.")

    return input_filename, output_filename, line_length, sentences_per_paragraph


# -----------------------------
# USER PROMPTS
# -----------------------------
def get_line_length(default=70):
    """Prompt user for line length if not provided."""
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
            print('Please enter a valid number (e.g., 50, 80, 100).')


def get_sentences_per_paragraph(default=3):
    """Prompt user for number of sentences per paragraph."""
    while True:
        try:
            user_input = input(f"How many sentences per paragraph would you like (default {default}): ").strip()
            if user_input == "":
                return default
            count = int(user_input)
            if count <= 0:
                print("Please enter a positive number greater than 0.")
                continue
            return count
        except ValueError:
            print('Please enter a valid number (e.g., 2, 3, 5).')


# -----------------------------
# TEXT PROCESSING
# -----------------------------
def read_input_file(filename):
    """Read entire input file content."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except Exception as e:
        sys.exit(f"Error reading input file: {e}")

    if not content:
        sys.exit(f"Error: Input file is empty: {filename}")

    return content


def split_into_sentences(text):
    """Split text into sentences using regex."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if s.strip()]


def group_sentences_into_paragraphs(sentences, max_sentences_per_paragraph):
    """Group sentences into paragraphs based on user input."""
    paragraphs = []
    for i in range(0, len(sentences), max_sentences_per_paragraph):
        paragraph = " ".join(sentences[i:i + max_sentences_per_paragraph])
        paragraphs.append(paragraph)
    return paragraphs


def reformat_text(content, line_length, sentences_per_paragraph):
    """Reformat text into wrapped paragraphs based on user-defined settings."""
    try:
        text = " ".join(content.split())  # Collapse extra whitespace
        sentences = split_into_sentences(text)
        paragraphs = group_sentences_into_paragraphs(sentences, sentences_per_paragraph)

        wrapped_paragraphs = [
            textwrap.fill(paragraph, width=line_length) for paragraph in paragraphs
        ]

        return "\n\n".join(wrapped_paragraphs)
    except Exception as e:
        sys.exit(f"Error reformatting text: {e}")


def write_output_file(filename, text):
    """Write reformatted text to output file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        sys.exit(f"Error writing output file: {e}")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    input_filename, output_filename, line_length, sentences_per_paragraph = validate_args()

    # Ask interactively if missing
    if line_length is None:
        line_length = get_line_length(default=70)
    if sentences_per_paragraph is None:
        sentences_per_paragraph = get_sentences_per_paragraph(default=3)

    content = read_input_file(input_filename)
    new_text = reformat_text(content, line_length, sentences_per_paragraph)
    write_output_file(output_filename, new_text)

    print(f"\n✅ Successfully wrote formatted text to: {output_filename}")
    print(f"   Each line is up to {line_length} characters long.")
    print(f"   Each paragraph has {sentences_per_paragraph} sentences.\n")


if __name__ == "__main__":
    main()
