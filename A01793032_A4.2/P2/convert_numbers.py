"""
convert_numbers.py

This script converts numeric values from an input file to their binary 
and hexadecimal representations and writes the results to an output file. 
Non-numeric values are skipped with a warning.

Usage:
    python3 convert_numbers.py P2

Author: Alejandra Mendoza Flores
Date: February 2, 2024
"""

import sys
import time

def read_numbers(input_file):
    """
    Reads numeric values from an input file and returns a list of integers.

    Parameters:
    - input_file (str): The path to the input file containing numeric values.

    Returns:
    - list: List of integers read from the input file.
    """
    try:
        with open(input_file, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        numbers = []
        for num_str in lines:
            num_str = num_str.strip()
            if num_str.isdigit() or (num_str.startswith('-') and num_str[1:].isdigit()):
                numbers.append(int(num_str))
            else:
                print(f"Warning: Skipping non-numeric value '{num_str}' in the input file.")
        return numbers

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None

def convert_numbers(input_file, output_file):
    """
    Converts numeric values to their binary and hexadecimal representations
    and writes the results to an output file.

    Parameters:
    - input_file (str): The path to the input file containing numeric values.
    - output_file (str): The path to the output file where conversion results will be stored.

    Returns:
    None
    """
    numbers = read_numbers(input_file)

    if numbers is None:
        return

    results = []

    for num in numbers:
        num_str = f"{num: < {max(len(str(max(numbers))), len('NUM'))}}"
        bin_str = f"{bin(num): <{max(len(str(max(numbers))), len('BIN'))}}"
        hex_str = f"{hex(num):<{max(len(str(max(numbers))), len('HEX'))}}"

        results.append((num_str, bin_str, hex_str))

    max_len_num = max(len(row[0]) for row in results)
    max_len_bin = max(len(row[1]) for row in results)
    max_len_hex = max(len(row[2]) for row in results)

    header = f"{'NUM':<{max_len_num}} | {'BIN':<{max_len_bin}} | {'HEX':<{max_len_hex}}"
    line = "-" * (max_len_num + max_len_bin + max_len_hex + 6)

    try:
        with open(output_file, 'a', encoding="utf-8") as result_file:
            result_file.write(f"File Used: {input_file.rsplit('.', 1)[0]}\n")
            result_file.write(header + "\n")
            result_file.write(line + "\n")

            for num_str, bin_str, hex_str in results:
                row = f"{num_str} | {bin_str} | {hex_str}"
                result_file.write(row + "\n")

            result_file.write(line + "\n")

    except FileNotFoundError:
        print(f"Error: File '{output_file}' not found.")

def main():
    """
    Main function to execute the conversion of numeric values from the command line.

    Usage:
    python convert_numbers.py input.txt

    Parameters:
    None

    Returns:
    None
    """
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py P2")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "ConversionResults.txt"

    numbers = read_numbers(input_file)
    if numbers is not None:
        convert_numbers(input_file, output_file)

        end_time = time.time()
        elapsed_time = end_time - start_time

        with open(output_file, 'a', encoding="utf-8") as result_file:
            result_file.write(f"\nTime Elapsed: {elapsed_time} seconds\n\n\n")
        print(f"Execution completed in {elapsed_time} segs. Results are stored in '{output_file}'.")
        print()

if __name__ == "__main__":
    main()
