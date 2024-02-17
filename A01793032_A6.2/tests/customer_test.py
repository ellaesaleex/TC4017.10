"""
Unit Test Script for Customer Management System

This script contains unit tests for the Customer class
in the Customer Management System. The tests cover various
functionalities such as creating, deleting, displaying,
and modifying customer information.

Test Cases:
- `test_create_customer`: Verifies that the `create_customer`
method creates a customer object with the correct attributes.
- `test_delete_customer`: Tests the deletion of a customer,
including successful deletion and handling of non-existent customers.
- `test_display_customer_info`: Checks the `display_customer_info`
method to ensure it logs the expected customer information.
- `test_modify_customer_info`: Tests the modification of customer
information using the `modify_customer_info` method.

Test Setup:
- The `setUp` method clears the content of 'customers.json'
before each test.

Logging Configuration:
- The `logging.basicConfig` method is used to configure logging
at the 'INFO' level.

Note: Ensure that the script is executed from the appropriate
directory to maintain proper file and module imports.

Usage:
- Run the script using `python3 -m unittest <script_name>`.

Author: Alejandra Mendoza Flores
Date: February 13, 2024
"""
import unittest
import logging
# pylint: disable=wrong-import-position, import-error
from src.customer.customer import Customer
logging.basicConfig(level=logging.INFO)
# pylint: enable=wrong-import-position, import-error


class CustomerTest(unittest.TestCase):
    """
    Unit tests for the Customer class.
    """
    def setUp(self):
        # Clear the content of customers.json before each test
        with open("customers.json", "w", encoding="utf-8") as file:
            file.write("[]")

    def test_create_customer(self):
        """
        Test case for the create_customer method of the Customer class.
        It verifies that a customer object is created
        with the correct attributes.
        """
        customer = Customer.create_customer("John Doe",
                                            "john@example.com", "1234567890")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
        self.assertEqual(customer.phone, "1234567890")

    def test_delete_customer(self):
        """
        Test case for deleting a customer.

        This test case verifies that the delete_customer method correctly
        deletes a customer from the system.
        It first creates a customer with the name "Jane Doe",
        email "jane@example.com", and phone number "9876543210".
        Then, it attempts to delete the customer with the name "Jane Doe"
        and asserts that the customer is deleted successfully.
        Finally, it attempts to delete a non-existent customer and asserts
        that the appropriate log message is generated.
        """
        Customer.create_customer("Jane Doe", "jane@example.com", "9876543210")
        Customer.delete_customer("Jane Doe")
        with self.assertLogs(level='INFO') as cm:
            Customer.delete_customer("Non-Existent Customer")
        self.assertIn("Customer not found.", cm.output[0])

    def test_display_customer_info(self):
        """
        Test case to verify the display_customer_info method
        of the Customer class.

        It creates a customer with the name "Alice", email "alice@example.com",
        and phone number "5551234567".
        Then, it asserts that the log output contains
        the expected customer name.
        """
        Customer.create_customer("Alice", "alice@example.com", "5551234567")
        with self.assertLogs(level='INFO') as cm:
            Customer.display_customer_info("Alice")
        self.assertIn("Customer Name: Alice", cm.output[0])

    def test_modify_customer_info(self):
        """
        Test case for modifying customer information.
        """
        Customer.create_customer("Bob",
                                 "bob@example.com",
                                 "9998887776")
        Customer.modify_customer_info("Bob",
                                      email="newbob@example.com",
                                      phone="1112233445")
        self.assertEqual(
            Customer.load_customers_data()[0]["email"], "newbob@example.com")
        self.assertEqual(
            Customer.load_customers_data()[0]["phone"], "1112233445")


if __name__ == '__main__':
    unittest.main()
