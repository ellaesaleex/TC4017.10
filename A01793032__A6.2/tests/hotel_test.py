"""
hotel_test.py - Unit Tests for the Hotel Class

This module contains a set of unit tests for validating the functionality
of the Hotel class in the 'hotel.py' module. The tests cover various aspects
of hotel creation, modification, reservation, and deletion.

Test Cases:
    - test_create_hotel: Tests the creation of a new hotel instance.
    - test_delete_hotel: Tests the deletion of a hotel instance.
    - test_display_info: Tests the display_info method of the Hotel class.
    - test_modify_info: Tests the modify_info method of the Hotel class.
    - test_reserve_room: Tests the reserve_room method of the Hotel class.
    - test_cancel_reservation: Tests the cancel_reservation
    method of the Hotel class.

Each test case is designed to assert the correct behavior of the Hotel class
methods under different scenarios. The setUp method ensures a consistent
starting point for each test by creating a test instance of the Hotel class.

To run the tests, execute the script using the following command:
    python3 -m unittest hotel_test.py

Author: Alejandra Mendoza Flores
Date: February 13, 2024
"""
import unittest
import sys
import os
# pylint: disable=wrong-import-position, import-error
#from src.hotel.hotel import Hotel
#from src.reservation.reservation import Reservation
# pylint: enable=wrong-import-position, import-error
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.hotel.hotel import Hotel
from src.reservation.reservation import Reservation

class HotelTest(unittest.TestCase):
    """
    Unit tests for the Hotel class.
    """

    def setUp(self):
        self.test_hotel = Hotel("Test Hotel", "Test Location", 10)

    def test_create_hotel(self):
        """
        Test case for the create_hotel method.

        This test verifies that the create_hotel method correctly
        creates a new hotel object with the specified name, location,
        and number of rooms.
        """
        new_hotel = Hotel.create_hotel("New Hotel", "New Location", 20)
        self.assertEqual(new_hotel.name, "New Hotel")
        self.assertEqual(new_hotel.location, "New Location")
        self.assertEqual(new_hotel.rooms, 20)

    def test_delete_hotel(self):
        """
        Test case to verify the behavior of the delete_hotel method.

        It creates a hotel, attempts to delete a non-existent hotel,
        and checks if the appropriate log message is generated.
        """
        Hotel.create_hotel("To Be Deleted Hotel", "Delete Location", 5)
        with self.assertLogs(level='INFO') as cm:
            Hotel.delete_hotel("Non-Existent Hotel")
        self.assertIn("INFO:root:Hotel Non-Existent Hotel not found for deletion.", cm.output[0])
        #self.assertIn("Hotel Non-Existent Hotel not found.", cm.output[0])

    def test_display_info(self):
        """
        Test case to verify the display_info method of the Hotel class.

        It asserts that the log output contains the expected
        information about the hotel.
        """
        with self.assertLogs(level='INFO') as cm:
            self.test_hotel.display_info()
        self.assertIn("Hotel Name: Test Hotel", cm.output[0])

    def test_modify_info(self):
        """
        Test case for modifying hotel information.
        """
        self.test_hotel.modify_info(name="Modified Hotel",
                                    location="Modified Location",
                                    rooms=15)
        self.assertEqual(self.test_hotel.name, "Modified Hotel")
        self.assertEqual(self.test_hotel.location, "Modified Location")
        self.assertEqual(self.test_hotel.rooms, 15)

    def test_reserve_room(self):
        """
        Test case for reserving a room in the hotel.

        This test creates a reservation object with the given details and
        attempts to reserve the room in the test hotel. It then checks if
        the reservation is added to the list of reservations in the hotel.
        """
        reservation = Reservation("John Doe", "Test Hotel", 101,
                                  "2024-02-14", "2024-02-18")
        self.test_hotel.reserve_room(reservation)
        self.assertIn(reservation, self.test_hotel.reservations)

    def test_cancel_reservation(self):
        """
        Test case for canceling a reservation.

        Creates a reservation, reserves a room in the hotel,
        cancels the reservation, and checks that the reservation
        is no longer in the hotel's list of reservations.
        """
        reservation = Reservation("John Doe", "Test Hotel", 101,
                                  "2024-02-14", "2024-02-18")
        self.test_hotel.reserve_room(reservation)
        self.test_hotel.cancel_reservation(reservation)
        self.assertNotIn(reservation, self.test_hotel.reservations)


if __name__ == '__main__':
    unittest.main()
