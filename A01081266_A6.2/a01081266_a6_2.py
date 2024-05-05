"""
A01081266 Ejercicio programacion 3
"""
import json
import os
import sys
import io
# Unit Tests
import unittest


class Hotel:
    """Class for representing a hotel"""
    def __init__(self, name, location):
        """hotel init"""
        self.name = name
        self.location = location
        self.rooms = []

    def add_room(self, room):
        """add rooms"""
        self.rooms.append(room)

    def remove_room(self, room):
        """remove rooms"""
        self.rooms.remove(room)

    def display_info(self):
        """display hotel info"""
        print("Hotel Name:", self.name)
        print("Location:", self.location)
        print("Number of Rooms:", len(self.rooms))
        print("Rooms:")
        for room in self.rooms:
            room.display_info()

    def to_json(self):
        """save in json file"""
        return {
            "name": self.name,
            "location": self.location,
            "rooms": [room.to_json() for room in self.rooms]
        }

    @staticmethod
    def from_json(json_data):
        """read json file"""
        hotel = Hotel(json_data['name'], json_data['location'])
        for room_data in json_data['rooms']:
            room = Room.from_json(room_data)
            hotel.add_room(room)
        return hotel


class Room:
    """Class for representing a hotel room"""
    def __init__(self, number, capacity):
        """init room"""
        self.number = number
        self.capacity = capacity

    def display_info(self):
        """Display room info"""
        print("Room Number:", self.number)
        print("Capacity:", self.capacity)

    def to_json(self):
        """save to json file"""
        return {
            "number": self.number,
            "capacity": self.capacity,
        }

    @staticmethod
    def from_json(json_data):
        """read from jason"""
        return Room(json_data['number'], json_data['capacity'])


class Customer:
    """Class for representing a customer"""
    def __init__(self, name, email):
        """init customer"""
        self.name = name
        self.email = email

    def display_info(self):
        """Display customer info"""
        print("Customer Name:", self.name)
        print("Email:", self.email)

    def to_json(self):
        """save to file"""
        return {
            "name": self.name,
            "email": self.email
        }

    @staticmethod
    def from_json(json_data):
        """read from"""
        return Customer(json_data['name'], json_data['email'])


class Reservation:
    """Class for representing a reservation"""
    def __init__(self, customer, hotel, room_number):
        """init reservation"""
        self.customer = customer
        self.hotel = hotel
        self.room_number = room_number

    def display_info(self):
        """display reservation info"""
        print("Reservation Details:")
        print("Customer:")
        self.customer.display_info()
        print("Hotel:")
        self.hotel.display_info()
        print("Room Number:", self.room_number)

    def to_json(self):
        """save to file"""
        return {
            "customer": self.customer.to_json(),
            "hotel": self.hotel.to_json(),
            "room_number": self.room_number
        }

    @staticmethod
    def from_json(json_data):
        """read from"""
        customer = Customer.from_json(json_data.get('customer', {}))
        hotel = Hotel.from_json(json_data.get('hotel', {}))
        room_number = json_data.get('room_number', None)
        # Verificar si 'rooms' existe en json_data
        if 'rooms' in json_data:
            # Si existe, obtener las habitaciones del hotel
            rooms = json_data['rooms']
            print("Rooms:", rooms)
        else:
            raise KeyError("'rooms' key not found in json_data")
        # Retornar la reservación con los datos obtenidos
        return Reservation(customer, hotel, room_number)


class HotelManager:
    """Class for manage the hotel"""
    def __init__(self):
        """init hotel manager"""
        self.hotels = []
        self.customers = []
        self.reservation = []

    def create_hotel(self, name, location):
        """Create hotel"""
        hotel = Hotel(name, location)
        self.hotels.append(hotel)

    def delete_hotel(self, hotel):
        """delete hotel"""
        self.hotels.remove(hotel)

    def display_hotel_info(self, hotel):
        """display hotel info"""
        hotel.display_info()

    def modify_hotel_info(self, hotel, name=None, location=None):
        """modify hotel info"""
        if name:
            hotel.name = name
        if location:
            hotel.location = location

    def add_room(self, hotel, room):
        """Agrega una habitación a un hotel"""
        hotel.add_room(room)

    def remove_room(self, hotel, room):
        """Agrega una habitación a un hotel"""
        hotel.remove_room(room)

    def reserve_room(self, customer, hotel, room_number):
        """reserve room"""
        reservation = Reservation(customer, hotel, room_number)
        self.reservation.append(reservation)

    def cancel_reservation(self, reservation):
        """cancel the reservation"""
        self.reservation.remove(reservation)

    def display_reservation_info(self, reservation):
        """display reservation info"""
        reservation.display_info()

    def create_customer(self, name, email):
        """create customer"""
        customer = Customer(name, email)
        self.customers.append(customer)

    def delete_customer(self, customer):
        """delete customer"""
        self.customers.remove(customer)

    def display_customer_info(self, customer):
        """display customer info"""
        customer.display_info()

    def modify_customer_info(self, customer, name=None, email=None):
        """modify customer info"""
        if name:
            customer.name = name
        if email:
            customer.email = email

    def save_data(self, filename):
        """save to json file"""
        data = {
            "hotels": [hotel.to_json() for hotel in self.hotels],
            "customers": [customer.to_json() for customer in self.customers],
            "reservations": [reservation.to_json()
                             for reservation in self.reservation]
        }
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file)
        except FileNotFoundError:
            print("Error: No se encontró el archivo.")

    def load_data(self, filename):
        """read data from json"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.hotels = [Hotel.from_json(hotel_data) for
                               hotel_data in data.get('hotels', [])]
                self.customers = [Customer.from_json(customer_data)
                                  for customer_data
                                  in data.get('customers', [])]
                self.reservation = [Reservation.from_json(reservation_data)
                                    for reservation_data
                                    in data.get('reservations', [])]


class HotelManagerTests(unittest.TestCase):
    """Class for test unit test cases"""
    def setUp(self):
        """set up the tests"""
        self.manager = HotelManager()
        self.hotel = Hotel("Hotel ABC", "Location XYZ")
        self.room = Room(101, 2)
        self.customer = Customer("John Doe", "john@example.com")
        self.reservation = Reservation(self.customer,
                                       self.hotel, self.room.number)
        self.filename = "test_data.json"

    def tearDown(self):
        """tear down the tests"""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_create_hotel(self):
        """create hotel test"""
        self.manager.create_hotel("Hotel ABC", "Location XYZ")
        self.assertEqual(len(self.manager.hotels), 1)

    def test_delete_hotel(self):
        """delete hotel test"""
        self.manager.hotels.append(self.hotel)
        self.manager.delete_hotel(self.hotel)
        self.assertEqual(len(self.manager.hotels), 0)

    def test_display_hotel_info(self):
        """display hotel info test"""
        self.manager.hotels.append(self.hotel)
        self.assertEqual(self.manager.display_hotel_info(self.hotel), None)

    def test_modify_hotel_info(self):
        """modify_hotel_info test"""
        self.manager.hotels.append(self.hotel)
        self.manager.modify_hotel_info(self.hotel, name="New Name")
        self.manager.modify_hotel_info(self.hotel, location="New location")
        self.assertEqual(self.hotel.name, "New Name")
        self.assertEqual(self.hotel.location, "New location")

    def test_reserve_room(self):
        """test_reserve_room test"""
        self.manager.customers.append(self.customer)
        self.manager.hotels.append(self.hotel)
        self.manager.reserve_room(self.customer, self.hotel, self.room.number)
        self.assertEqual(len(self.manager.reservation), 1)

    def test_cancel_reservation(self):
        """test_cancel_reservation test"""
        reservation = Reservation(self.customer, self.hotel, self.room.number)
        self.manager.reservation.append(reservation)
        self.manager.cancel_reservation(reservation)
        self.assertEqual(len(self.manager.reservation), 0)

    def test_create_customer(self):
        """test_cancel_reservation test"""
        self.manager.create_customer("John Doe", "john@example.com")
        self.assertEqual(len(self.manager.customers), 1)

    def test_delete_customer(self):
        """test_cancel_reservation test"""
        self.manager.customers.append(self.customer)
        self.manager.delete_customer(self.customer)
        self.assertEqual(len(self.manager.customers), 0)

    def test_display_customer_info(self):
        """test_cancel_reservation test"""
        self.manager.customers.append(self.customer)
        self.assertEqual(self.manager.display_customer_info(self.customer),
                         None)

    def test_modify_customer_info(self):
        """test_cancel_reservation test"""
        self.manager.customers.append(self.customer)
        self.manager.modify_customer_info(self.customer, name="New Name")
        self.manager.modify_customer_info(self.customer, email="New@mail.com")
        self.assertEqual(self.customer.name, "New Name")
        self.assertEqual(self.customer.email, "New@mail.com")

    def test_display_reservation_info(self):
        """display reservation info test"""
        self.manager.customers.append(self.customer)
        self.manager.hotels.append(self.hotel)
        self.manager.reserve_room(self.customer, self.hotel, self.room.number)
        self.assertEqual(self.manager.display_reservation_info
                         (self.reservation), None)

    def test_add_room(self):
        """Test add_room method"""
        self.manager.create_hotel("Hotel ABC", "Location XYZ")
        self.manager.add_room(self.hotel, self.room)
        self.assertIn(self.room, self.hotel.rooms)

    def test_remove_room(self):
        """Test remove_room method"""
        self.manager.create_hotel("Hotel ABC", "Location XYZ")
        self.manager.add_room(self.hotel, self.room)
        self.assertIn(self.room, self.hotel.rooms)
        self.manager.remove_room(self.hotel, self.room)
        self.assertNotIn(self.room, self.hotel.rooms)

    def test_save_and_load_data(self):
        """Test save_data and load_data methods"""
        # Datos de prueba para guardar
        self.manager.create_hotel("Hotel Test", "Location Test")
        self.manager.create_customer("John Doe", "john@example.com")
        self.manager.reserve_room(self.manager.customers[0],
                                  self.manager.hotels[0], 101)
        # Guardar los datos en un archivo
        self.manager.save_data(self.filename)
        # Cargar los datos desde el archivo
        self.manager.load_data(self.filename)
        # Verificar si los datos cargados son los mismos que los guardados
        self.assertEqual(len(self.manager.hotels), 1)
        self.assertEqual(self.manager.hotels[0].name, "Hotel Test")
        self.assertEqual(self.manager.hotels[0].location, "Location Test")
        self.assertEqual(len(self.manager.customers), 1)
        self.assertEqual(self.manager.customers[0].name, "John Doe")
        self.assertEqual(self.manager.customers[0].email, "john@example.com")
        self.assertEqual(len(self.manager.reservation), 1)
        self.assertEqual(self.manager.reservation[0].room_number, 101)


class RoomTests(unittest.TestCase):
    """Class for test unit test cases for Room"""
    def setUp(self):
        """set up the tests"""
        self.room = Room(101, 2)
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """tear down the tests"""
        sys.stdout = sys.__stdout__

    def test_display_info(self):
        """Test display_info method"""
        expected_output = "Room Number: 101\nCapacity: 2\n"
        self.room.display_info()
        actual_output = self.captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)


class HotelTests(unittest.TestCase):
    """Class for test unit test cases for Hotel"""
    def test_from_json(self):
        """Test from_json method"""
        # Datos de prueba para un hotel en formato JSON
        json_data = {
            "name": "Hotel Test",
            "location": "Location Test",
            "rooms": [
                {"number": 101, "capacity": 2},
                {"number": 102, "capacity": 3}
            ]
        }
        # Convertir JSON a objeto Hotel
        hotel = Hotel.from_json(json_data)
        # Verificar si los datos se han cargado correctamente
        self.assertEqual(hotel.name, "Hotel Test")
        self.assertEqual(hotel.location, "Location Test")
        self.assertEqual(len(hotel.rooms), 2)
        self.assertEqual(hotel.rooms[0].number, 101)
        self.assertEqual(hotel.rooms[0].capacity, 2)
        self.assertEqual(hotel.rooms[1].number, 102)
        self.assertEqual(hotel.rooms[1].capacity, 3)
        # Casos de prueba negativos
        # 1. Intentar agregar una habitación que no es un objeto Room
        hotel = Hotel("Hotel Test", "Location Test")
        with self.assertRaises(AttributeError):
            hotel.add_room("Not a room")
        # 2. Intentar eliminar una habitación que no existe
        hotel = Hotel("Hotel Test", "Location Test")
        room = Room(101, 2)
        hotel.add_room(room)
        with self.assertRaises(ValueError):
            hotel.remove_room(Room(102, 2))
        # 3. Intentar crear un hotel sin especificar un nombre
        with self.assertRaises(TypeError):
            hotel = Hotel(None, "Location Test")
        # 4. Intentar crear un hotel sin especificar una ubicación
        with self.assertRaises(TypeError):
            hotel = Hotel("Hotel Test", None)
        # 5. Intentar crear un hotel sin especificar ni nombre ni ubicación
        with self.assertRaises(TypeError):
            hotel = Hotel(None, None)


class ReservationTests(unittest.TestCase):
    """Class for test unit test cases for Reservation"""
    def test_from_json(self):
        """Test from_json method"""
        # Datos de prueba para una reserva en formato JSON
        json_data = {
            "customer": {"name": "John Doe", "email": "john@example.com"},
            "hotel": {"name": "Hotel Test", "location": "Location Test"},
            "room_number": 101
        }
        # Convertir JSON a objeto Reservation
        reservation = Reservation.from_json(json_data)
        # Verificar si los datos se han cargado correctamente
        self.assertEqual(reservation.customer.name, "John Doe")
        self.assertEqual(reservation.customer.email, "john@example.com")
        self.assertEqual(reservation.hotel.name, "Hotel Test")
        self.assertEqual(reservation.hotel.location, "Location Test")
        self.assertEqual(reservation.room_number, 101)


if __name__ == '__main__':
    unittest.main()
