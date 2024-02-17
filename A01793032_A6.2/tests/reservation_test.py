"""
Module: reservation_test.py

This module contains unit tests for the Reservation class,
which is a part of a hotel reservation management system.

The Reservation class provides functionality for creating
reservations, canceling reservations, and loading reservations data
from a JSON file. Each reservation includes information such as
the customer's name, hotel name, room number, check-in date,
and check-out date.

The unit tests in this module cover various aspects
of the Reservationclass, including the creation
of reservations, cancellation of reservations, and loading
of reservations data.

Usage:
- Execute this module to run the unit tests for the Reservation class.

Note:
- Ensure that the 'reservations.json' file is present and writable
for successful execution of tests involving data loading.

Author: Alejandra Mendoza Flores
Date: February 13, 2024

"""
import unittest
# pylint: disable=wrong-import-position, import-error
from src.reservation.reservation import Reservation
# pylint: enable=wrong-import-position, import-error


class ReservationTest(unittest.TestCase):
    """
    Test case for the Reservation class.
    """
    def setUp(self):
        with open("reservations.json", "w", encoding="utf-8") as file:
            file.write("[]")

    def test_create_reservation(self):
        """
        Test case for the create_reservation method of the Reservation class.
        It verifies that a reservation is created with the correct attributes.
        """
        reservation = Reservation.create_reservation("John Doe",
                                                     "Test Hotel",
                                                     101,
                                                     "2024-02-14",
                                                     "2024-02-18")
        self.assertEqual(reservation.customer_name, "John Doe")
        self.assertEqual(reservation.hotel_name, "Test Hotel")
        self.assertEqual(reservation.room_number, 101)
        self.assertEqual(reservation.check_in_date, "2024-02-14")
        self.assertEqual(reservation.check_out_date, "2024-02-18")

    def test_cancel_reservation(self):
        """
        Test case for cancel_reservation method of Reservation class.
        It verifies that the reservation is canceled successfully and that
        an appropriate log message is generated when the reservation
        is not found.
        """
        Reservation.create_reservation("Alice",
                                       "Another Hotel",
                                       102,
                                       "2024-03-01",
                                       "2024-03-10")
        Reservation.cancel_reservation("Alice",
                                       "Another Hotel",
                                       102,
                                       "2024-03-01")
        with self.assertLogs(level='WARNING') as cm:
            Reservation.cancel_reservation(
                "Non-Existent", "Hotel", 103, "2024-03-02")
        self.assertIn("Reservation not found.", cm.output[0])

    def test_load_reservations_data(self):
        """
        Test case for the load_reservations_data method.

        This test case verifies that the load_reservations_data
        method correctly loads the reservations data
        and returns a list of reservations.

        It creates a reservation, loads the reservations data,
        and asserts that the loaded data matches the created reservation.

        """
        Reservation.create_reservation("Bob", "Yet Another Hotel", 103,
                                       "2024-04-01", "2024-04-05")
        reservations_data = Reservation.load_reservations_data()
        self.assertEqual(len(reservations_data), 1)
        self.assertEqual(reservations_data[0]["customer_name"], "Bob")
        self.assertEqual(reservations_data[0]["hotel_name"],
                         "Yet Another Hotel")
        self.assertEqual(reservations_data[0]["room_number"], 103)
        self.assertEqual(reservations_data[0]["check_in_date"], "2024-04-01")
        self.assertEqual(reservations_data[0]["check_out_date"], "2024-04-05")


if __name__ == '__main__':
    unittest.main()
