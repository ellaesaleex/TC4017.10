"""
compute_statistics.py

This script reads numeric data from a file, computes various statistics 
(mean, median, mode, variance, and standard deviation), and prints the results. 
It also saves the results to a file.

Usage:
    python3 compute_statistics.py P1

Author: Alejandra Mendoza Flores
Date: February 2, 2024
"""
import sys
import time

def read_file(file_path):
    """
    Read numeric data from a file and return a list of values.

    Parameters:
    - file_path (str): Path to the file containing numeric data.

    Returns:
    - list or None: List of numeric values read from the file.
    Returns None if the file is not found.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = []
            for line in file.readlines():
                line = line.strip()
                try:
                    float_value = float(line)
                    data.append(float_value)
                except ValueError:
                    print(f"Warning: Skipping non-numeric entry in '{file_path}': {line}")
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def calculate_mean(data):
    """
    Calculate the mean (average) of a list of numeric values.

    Parameters:
    - data (list of float): List containing numeric values.

    Returns:
    - float or None: The mean value if the data is not empty, otherwise None.
    """
    return sum(data) / len(data) if data else None

def calculate_median(data):
    """
    Calculate the median of a list of numeric values.

    Parameters:
    - data (list of float): List containing numeric values.

    Returns:
    - float: The median value of the numeric data.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    return (sorted_data[mid] + sorted_data[mid - 1]) / 2 if n % 2 == 0 else sorted_data[mid]

def calculate_mode(data):
    """
    Calculate the mode of a list of numeric values.

    Parameters:
    - data (list of float): List containing numeric values.

    Returns:
    - list or str: List of mode values if they exist, otherwise "N/A".
    """
    frequency = {}
    for number in data:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values(), default=0)
    return [k for k, v in frequency.items() if v == max_frequency] if max_frequency > 1 else "N/A"

def calculate_variance(data, mean):
    """
    Calculate the variance of a list of numeric values.

    Parameters:
    - data (list of float): List containing numeric values.
    - mean (float): The mean (average) of the numeric values.

    Returns:
    - float or None: The variance value if the data has more than one element, otherwise None.
    """
    n = len(data)
    return sum((x - mean) ** 2 for x in data) / n if n > 1 else None

def calculate_std_dev(variance):
    """
    Calculate the standard deviation from the given variance.

    Parameters:
    - variance (float or None): The variance value. If None, the result will be None.

    Returns:
    - float or None: The standard deviation if variance is not None, otherwise None.
    """
    return (variance ** 0.5) if variance is not None else None


def print_results(mean, median, mode, variance, std_dev):
    """
    Print the calculated statistics to the console.

    Parameters:
    - mean (float or None): The mean value.
    - median (float): The median value.
    - mode (list or str): List of mode values or "N/A" if there is no mode.
    - variance (float or None): The variance value.
    - std_dev (float or None): The standard deviation value.
    """
    print(f"Mean: {mean:.5f}")
    print(f"Median: {median}")
    print(f"Mode: {mode if mode else 'N/A'}")
    print(f"Variance: {variance:.3f}")
    print(f"Standard Deviation: {std_dev:.5f}")
    print()


def main():
    """
    Calculate statistics from numeric data in a file and print/save the results.

    This function serves as the main entry point for the compute_statistics.py script.
    It reads a file path from the command line, calculates various statistics
    (mean, median, mode, variance, and standard deviation) from the numeric data in the file,
    and prints the results to the console. Additionally, it saves the results to a file.

    Usage:
        python3 compute_statistics.py input_file

    Parameters:
        None (Uses command line arguments for input file)

    Returns:
        None

    Raises:
        SystemExit: If the command line arguments are not provided correctly.

    """
    if len(sys.argv) != 2:
        print("Usage: python3 compute_statistics.py P1")
        sys.exit(1)

    input_file = sys.argv[1]
    file_name = input_file.split('.')[0]
    data = read_file(input_file)

    if data:
        start = time.time()

        mean = calculate_mean(data)
        median = calculate_median(data)
        mode = calculate_mode(data)
        variance = calculate_variance(data, mean)
        std_dev = calculate_std_dev(variance)

        end = time.time()
        elapsed_time = end - start

        count_values = len(data)

        print(f"File Used: {file_name}")
        print(f"Lines:\t{len(data)}")
        print(f"Count:\t{count_values}")
        print(f"Elapsed Time: {elapsed_time} seconds")

        print_results(mean, median, mode, variance, std_dev)

        with open("StatisticsResults.txt", 'a', encoding='utf-8') as file:
            count_values = len(data)

            file.write(f"{'Statistic': <20} {'Value': <20}\n")
            file.write(f"{'Count': <20} {count_values}\n")
            file.write(f"{'Mean': <20} {mean:.5f}\n")
            file.write(f"{'Median': <20} {median}\n")
            file.write(f"{'Mode': <20} {mode}\n")
            file.write(f"{'Variance': <20} {variance:.3f}\n")
            file.write(f"{'Standard Deviation': <20} {std_dev:.5f}\n")
            file.write(f"{'Elapsed Time': <20} {elapsed_time:.5f} s\n\n")

if __name__ == "__main__":
    main()
