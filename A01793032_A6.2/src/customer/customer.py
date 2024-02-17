"""
Module Description:

This module defines the Customer class,
representing a customer in a simple
Customer Management System.
It provides methods for creating, deleting,
displaying information, and modifying customer details.
Customer data is stored in a JSON file ('customers.json').

Classes:
    - Customer: Represents a customer and provides methods
    for customer management.

Methods:
    - create_customer(name, email, phone): Creates a new customer
    and saves it to 'customers.json'.
    - delete_customer(name): Deletes a customer from 'customers.json'
    based on the given name.
    - display_customer_info(name): Displays information about a customer.
    - modify_customer_info(name, email=None, phone=None):
    Modifies customer information.
    - load_customers_data(): Loads customer data
    from 'customers.json'.

Usage:
    - To use this module, create an instance of the Customer class
    and call its methods as needed.

Example:
    customer_instance = Customer("John Doe", "john@example.com",
    "123-456-7890")
    customer_instance.create_customer("Jane Smith", "jane@example.com",
    "987-654-3210")
    customer_instance.display_customer_info("Jane Smith")
    customer_instance.modify_customer_info("Jane Smith",
    email="new_jane@example.com")

Author: Alejandra Mendoza Flores
Date: February 13, 2024
"""
import os
import json
import logging


class Customer:
    """
    Represents a customer.

    Attributes:
        name (str): The name of the customer.
        email (str): The email of the customer.
        phone (str): The phone number of the customer.
    """

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    @staticmethod
    def create_customer(name, email, phone):
        """
        Creates a new customer and saves it to the customers.json file.

        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.
            phone (str): The phone number of the customer.

        Returns:
            Customer: The newly created customer.
        """
        new_customer = Customer(name, email, phone)
        customers_data = []
        if os.path.exists("customers.json"):
            with open("customers.json", "r", encoding="utf-8") as file:
                customers_data = json.load(file)
        customers_data.append({
            "name": new_customer.name, "email": new_customer.email,
            "phone": new_customer.phone})
        with open("customers.json", "w", encoding="utf-8") as file:
            json.dump(customers_data, file)

        return new_customer

    @staticmethod
    def delete_customer(name):
        """
        Deletes a customer from the customers.json file.

        Args:
            name (str): The name of the customer to delete.

        Returns:
            None
        """
        customers_data = Customer.load_customers_data()
        filtered_customers = [
            customer for customer in customers_data if customer["name"] != name
            ]
        if len(filtered_customers) < len(customers_data):
            with open("customers.json", "w", encoding="utf-8") as file:
                json.dump(filtered_customers, file)
            logging.info("Customer %s deleted successfully.", name)
        else:
            logging.info("Customer %s not found.", name)

    @staticmethod
    def display_customer_info(name):
        """
        Displays the information of a customer.

        Args:
            name (str): The name of the customer to display.

        Returns:
            None
        """
        customers_data = Customer.load_customers_data()
        customer = next(
            (customer for customer in customers_data
             if customer["name"] == name),
            None)
        if customer:
            logging.info("Customer Name: %s", customer['name'])
            logging.info("Email: %s", customer['email'])
            logging.info("Phone: %s", customer['phone'])
        else:
            logging.info("Customer %s not found.", name)

    @staticmethod
    def modify_customer_info(name, email=None, phone=None):
        """
        Modifies the information of a customer.

        Args:
            name (str): The name of the customer to modify.
            email (str, optional): The new email of the customer.
            Defaults to None.
            phone (str, optional): The new phone number of the customer.
            Defaults to None.

        Returns:
            None

        Raises:
            None
        """
        customers_data = Customer.load_customers_data()
        customer = next(
            (customer for customer in customers_data
             if customer["name"] == name),
            None)
        if customer:
            if email:
                customer["email"] = email
            if phone:
                customer["phone"] = phone
            with open("customers.json", "w", encoding="utf-8") as file:
                json.dump(customers_data, file)
            print(f"Customer {name} information modified successfully.")
        else:
            print(f"Customer {name} not found.")

    @staticmethod
    def load_customers_data():
        """
        Load customer data from a JSON file.

        Returns:
            list: A list of customer data.

        Raises:
            FileNotFoundError: If the customers.json file does not exist.
        """
        if os.path.exists("customers.json"):
            with open("customers.json", "r", encoding="utf-8") as file:
                return json.load(file)
        raise FileNotFoundError("The customers.json file does not exist.")
