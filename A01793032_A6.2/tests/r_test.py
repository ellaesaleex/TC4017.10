"""
Hotel Reservation System - Unit Tests

This module contains unit tests for the Reservation class,
which is a part of a hotel reservation management system.
The tests cover the creation, cancellation, and data loading
functionality of reservations.

Test Cases:
1. test_create_reservation: Verifies the correct creation of a reservation.
2. test_cancel_reservation: Tests the cancellation of reservations.
3. test_load_reservations_data: Verifies the loading of reservations data.

Note:
- Ensure the 'reservations.json' file is present and writable
for successful testing.

Author: Alejandra Mendoza Flores
Date: February 13, 2024
"""
import unittest
from unittest.mock import patch
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

    def tearDown(self):
        # Limpiar cualquier dato creado durante las pruebas
        pass

    def test_create_reservation(self):
        """
        Test case for the create_reservation method.

        This test verifies that the create_reservation method
        correctly creates a reservation object with the given parameters.
        It checks if the customer name, hotel name, room number,
        check-in date, and check-out date of the created reservation
        match the expected values.
        """
        reservation = Reservation.create_reservation(
            "John Doe", "Test Hotel", 101, "2024-02-14", "2024-02-18")
        self.assertEqual(reservation.customer_name, "John Doe")
        self.assertEqual(reservation.hotel_name, "Test Hotel")
        self.assertEqual(reservation.room_number, 101)
        self.assertEqual(reservation.check_in_date, "2024-02-14")
        self.assertEqual(reservation.check_out_date, "2024-02-18")

    def test_cancel_reservation(self):
        """
        Test case for canceling a reservation.

        This test case verifies the behavior of the cancel_reservation method
        in the Reservation class.
        It creates a reservation, cancels it, and then attempts to cancel
        a non-existent reservation.
        """
        Reservation.create_reservation(
            "Alice", "Another Hotel", 102, "2024-03-01", "2024-03-10")
        Reservation.cancel_reservation(
            "Alice", "Another Hotel", 102, "2024-03-01")
        m_pa = "src.reservation.reservation.Reservation.load_reservations_data"
        with patch(m_pa, return_value=[]):
            Reservation.cancel_reservation(
                "Non-Existent", "Hotel", 103, "2024-03-02")

    def test_load_reservations_data(self):
        """
        Test case for the load_reservations_data method.

        This test case verifies that the load_reservations_data
        method returns the correct reservations data.
        It creates a reservation, loads the reservations data,
        and asserts that the loaded data matches the created reservation.

        """
        Reservation.create_reservation(
            "Bob", "Yet Another Hotel", 103, "2024-04-01", "2024-04-05")
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
