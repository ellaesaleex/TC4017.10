"""
hotel.py - Hotel Management System

This module defines the Hotel class, representing a simple
hotel with basic management functionalities.
It includes methods for creating, deleting, displaying information,
modifying details, reserving rooms, and canceling reservations.

Classes:
    - Hotel: Represents a hotel and provides methods for management tasks.

Methods:
    - create_hotel(name, location, rooms): Creates a new hotel object,
      saves it to a JSON file, and returns the created hotel.
    - delete_hotel(name): Deletes a hotel from the hotels.json file based
    on the given name.
    - display_info(): Displays information about the hotel, including
    its name, location, number of rooms, and reservations.
    - modify_info(name=None, location=None, rooms=None):
    Modifies the information of the hotel.
    - reserve_room(reservation):
    Reserves a room and adds the reservation to the list.
    - cancel_reservation(reservation): Cancels an existing reservation.

Usage:
    - To use this module, create an instance of the
    Hotel class and call its methods as needed.

Example:
    hotel_instance = Hotel("Sample Hotel", "City Center", 50)
    hotel_instance.create_hotel("New Hotel", "Suburb", 30)
    hotel_instance.display_info()

"""
import os
import json
import logging


class Hotel:
    """
    Represents a hotel with its name, location, rooms, and reservations.

    Attributes:
    - name (str): The name of the hotel.
    - location (str): The location of the hotel.
    - rooms (int): The number of rooms in the hotel.
    - reservations (list): A list of reservations made for the hotel.

    Methods:
    - create_hotel(name, location, rooms):
    Creates a new hotel object and saves it to a JSON file.
    - delete_hotel(name):
    Deletes a hotel from the hotels.json file based on the given name.
    - display_info(): Displays information about the hotel, including its name,
    location, number of rooms, and reservations.
    - modify_info(name=None, location=None, rooms=None):
    Modifies the information of the hotel.
    - reserve_room(reservation):
    Reserves a room and adds it to the list of reservations.
    - cancel_reservation(reservation): Cancels an existing reservation.

    Author: Alejandra Mendoza Flores
    Date: February 13, 2024
    """
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    @staticmethod
    def create_hotel(name, location, rooms):
        """
        Creates a new hotel object and saves it to a JSON file.

        Parameters:
        name (str): The name of the hotel.
        location (str): The location of the hotel.
        rooms (int): The number of rooms in the hotel.

        Returns:
        Hotel: The newly created hotel object.
        """
        new_hotel = Hotel(name, location, rooms)
        hotels_data = []

        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as file:
                hotels_data = json.load(file)

        hotels_data.append({"name": new_hotel.name,
                            "location": new_hotel.location,
                            "rooms": new_hotel.rooms})

        with open("hotels.json", "w", encoding="utf-8") as file:
            json.dump(hotels_data, file)

        return new_hotel

    @staticmethod
    def delete_hotel(name):
        """
        Deletes a hotel from the hotels.json file based on the given name.

        Args:
            name (str): The name of the hotel to be deleted.

        Returns:
            None
        """
        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as file:
                hotels_data = json.load(file)

            filtered_hotels = [
                hotel for hotel in hotels_data if hotel["name"] != name
                ]

            if len(filtered_hotels) < len(hotels_data):
                with open("hotels.json", "w", encoding="utf-8") as file:
                    json.dump(filtered_hotels, file)
                logging.info("Hotel %s deleted successfully.", name)
            else:
                logging.info("Hotel %s not found for deletion.", name)
        else:
            logging.info("No hotels found.")

    def display_info(self):
        """
        Displays information about the hotel, including its name, location,
        number of rooms, and reservations.
        """
        logging.info("Hotel Name: %s", self.name)
        logging.info("Location: %s", self.location)
        logging.info("Number of Rooms: %s", self.rooms)
        logging.info("Reservations:")
        for reservation in self.reservations:
            logging.info(reservation)

    def modify_info(self, name=None, location=None, rooms=None):
        """
        Modifies the information of the hotel.

        Args:
            name (str, optional): The new name of the hotel. Defaults to None.
            location (str, optional): The new location of the hotel.
            Defaults to None.
            rooms (int, optional): The new number of rooms in the hotel.
            Defaults to None.
        """
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms

    def reserve_room(self, reservation):
        """
        Reserva una habitación y la agrega a la lista de reservaciones.

        Args:
            reservation (objeto): La reserva de habitación a agregar.

        Returns:
            None
        """
        self.reservations.append(reservation)

    def cancel_reservation(self, reservation):
        """
        Cancela una reserva existente.

        Parameters:
        reservation (objeto): La reserva a cancelar.

        Returns:
        None
        """
        if reservation in self.reservations:
            self.reservations.remove(reservation)
        else:
            print("Reservation not found.")
