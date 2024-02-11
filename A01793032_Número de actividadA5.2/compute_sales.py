"""
Sales Computation Script

This script reads product catalog and sales information from JSON files,
calculates the total sales amount, and writes the results to a text file.

Usage:
    python compute_sales.py catalog_json sales_json

Dependencies:
    - Python 3
    - Required Python modules: json, time, sys

Input:
    - catalog_json (str): Path to the JSON file
    containing product catalog information.
    - sales_json (str): Path to the JSON file
    containing sales information.

Output:
    - Prints total sales amount and elapsed time.
    - Writes total sales and elapsed time information
    to "sales_results.txt" file.

Example:
    python3 compute_sales.py catalog.json sales.json

Alumna: Alejandra Mendoza Flores
Matricula: A01793032
Date: February 7, 2024
"""

import sys
import json
import time

from os.path import exists


def read_products(catolog_json):
    """
    Reads and loads product data from a JSON file.

    Parameters:
    - catolog_json (str): The path to the JSON file
    containing product information.

    Returns:
    - dict: A dictionary representing the product data
    loaded from the JSON file.
    """
    with open(catolog_json, "r", encoding="utf-8") as file:
        return json.load(file)


def read_sales(sales_json):
    """
    Reads and loads sales data from a JSON file.

    Parameters:
    - sales_json (str): The path to the JSON file containing sales information.

    Returns:
    - dict: A dictionary representing the sales data loaded from the JSON file.
    """
    with open(sales_json, "r", encoding="utf-8") as file:
        return json.load(file)


def compute_sales(products, sales):
    """
    Calculates the total sales amount based on product
    information and sales data.

    Parameters:
    - products (list): A list of dictionaries representing
    product information.
    - sales (list): A list of dictionaries representing sales data,
    including product names and quantities.

    Returns:
    - float: The total sales amount calculated from the product prices
    and sales quantities.
    """
    total_sales = 0
    for sale in sales:
        name = sale["Product"]
        try:
            quantity = int(sale["Quantity"])
        except ValueError:
            print(f"Invalid quantity: {sale['sale']}")
            continue

        for product in products:
            if product["title"] == name:
                try:
                    price = float(product["price"])
                except ValueError:
                    print(f"Invalid price: {name}")
                    continue
                total_sales += price * quantity
                break
    return total_sales


def write_results(total_sales, elapsed):
    """
    Writes total sales and elapsed time information to a text file.

    Parameters:
    - total_sales (float): The total sales amount to be written to the file.
    - elapsed (float): The elapsed time (in seconds) to be written to the file.

    Returns:
    - None

    Writes to File:
    - The total sales amount formatted as "Total sales:   <total_sales>".
    - The elapsed time formatted as "Time:   <elapsed> seconds".
    """
    with open("sales_results.txt", "a", encoding="utf-8") as file:
        file.write(f"Total sales:\t${total_sales:.2f}\n")
        file.write(f"Time:\t\t{elapsed:.5f} sec\n\n")


def main():
    """
    Main function to compute and write sales information
    based on input JSON files.

    Usage:
    - python compute_sales.py catalog_json sales_json

    Parameters:
    - catalog_json (str): Path to the JSON file containing
    product catalog information.
    - sales_json (str): Path to the JSON file containing sales information.

    Prints:
    - Total sales amount.
    - Elapsed time for the computation.

    Writes to File:
    - Total sales and elapsed time information
    in a text file named "sales_results.txt".
    """
    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py catalog_json sales_json")
        sys.exit(1)

    start = time.time()

    catolog_json = sys.argv[1]
    sales_json = sys.argv[2]

    if not exists(catolog_json):
        print("File not found: ", catolog_json)
        sys.exit(1)

    if not exists(sales_json):
        print("File not found: ", sales_json)
        sys.exit(1)

    products = read_products(catolog_json)
    sales = read_sales(sales_json)

    total_sales = compute_sales(products, sales)

    end = time.time()
    elapsed = end - start

    write_results(total_sales, elapsed)

    print(f"Total sales:\t{total_sales:.2f}")
    print(f"Time:\t\t{elapsed:.5f} sec")


if __name__ == "__main__":
    main()
