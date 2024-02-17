"""
Module Description:

This module defines the Reservation class,
epresenting a hotelreservation in a simple
Reservation System.
It provides methods for creating,
canceling reservations, and loading reservation data
from a JSON file ('reservations.json').

Classes:
    - Reservation: Represents a hotel reservation
    and provides methods for reservation management.

Methods:
    - create_reservation(customer_name, hotel_name,
    room_number, check_in_date, check_out_date):
      Creates a new reservation and saves it to 'reservations.json'.
    - cancel_reservation(customer_name, hotel_name,
    room_number, check_in_date):
      Cancels a hotel reservation for a specific customer.
    - load_reservations_data(): Loads reservation data
    from 'reservations.json'.

Usage:
    - To use this module, create an instance of the
    Reservation class and call its methods as needed.

Example:
    reservation_instance =
    Reservation("John Doe", "Sample Hotel", 101, "2024-02-14", "2024-02-18")
    reservation_instance.create_reservation("Jane Smith",
    "Another Hotel", 201, "2024-03-01", "2024-03-05")
    reservation_instance.cancel_reservation("Jane Smith",
    "Another Hotel", 201, "2024-03-01")

Author: Alejandra Mendoza Flores
Date: February 13, 2024
"""
import os
import json
import logging


class Reservation:
    """
    Represents a hotel reservation.

    Attributes:
        customer_name (str): The name of the customer making the reservation.
        hotel_name (str): The name of the hotel where the reservation is made.
        room_number (str): The number of the room reserved.
        check_in_date (str): The date of check-in for the reservation.
        check_out_date (str): The date of check-out for the reservation.
    """

    def __init__(self, customer_name, hotel_name, room_number,
                 check_in_date, check_out_date=None):
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    @staticmethod
    def create_reservation(customer_name, hotel_name, room_number,
                           check_in_date, check_out_date=None):
        """
        Creates a new reservation and saves it to the reservations.json file.

        Args:
            customer_name (str): The name of the customer
            making the reservation.
            hotel_name (str): The name of the hotel where
            the reservation is being made.
            room_number (str): The number of the room being reserved.
            check_in_date (str): The date of check-in for the reservation.
            check_out_date (str): The date of check-out for the reservation.

        Returns:
            Reservation: The newly created reservation object.
        """
        new_reservation = Reservation(customer_name, hotel_name, room_number,
                                      check_in_date, check_out_date)
        reservations_data = []
        if os.path.exists("reservations.json"):
            with open("reservations.json", "r", encoding="utf-8") as file:
                reservations_data = json.load(file)
        reservations_data.append({
            "customer_name": new_reservation.customer_name,
            "hotel_name": new_reservation.hotel_name,
            "room_number": new_reservation.room_number,
            "check_in_date": new_reservation.check_in_date,
            "check_out_date": new_reservation.check_out_date
            })
        with open("reservations.json", "w", encoding="utf-8") as file:
            json.dump(reservations_data, file)
        return new_reservation

    @staticmethod
    def cancel_reservation(customer_name, hotel_name,
                           room_number, check_in_date):
        """
        Cancela una reserva de hotel para
        un cliente específico.

        Parámetros:
        - customer_name (str): Nombre del cliente.
        - hotel_name (str): Nombre del hotel.
        - room_number (int): Número de habitación.
        - check_in_date (str): Fecha de entrada en formato "YYYY-MM-DD".
        """
        reservations_data = Reservation.load_reservations_data()
        reservation_to_cancel = next(
            (reservation for reservation in reservations_data
                if reservation["customer_name"] == customer_name
                and reservation["hotel_name"] == hotel_name
                and reservation["room_number"] == room_number
                and reservation["check_in_date"] == check_in_date), None)

        if reservation_to_cancel:
            reservations_data.remove(reservation_to_cancel)
            with open("reservations.json", "w", encoding="utf-8") as file:
                json.dump(reservations_data, file)
            logging.info("Reservation canceled successfully.")
        else:
            logging.warning("Reservation not found.")

    @staticmethod
    def load_reservations_data():
        """
        Load reservations data from reservations.json file.

        Returns:
            list: A list of reservations data.
        """
        if os.path.exists("reservations.json"):
            with open("reservations.json", "r", encoding="utf-8") as file:
                return json.load(file)
        return []
