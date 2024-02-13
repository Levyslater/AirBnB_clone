import unittest
from models.place import Place
from datetime import datetime
import models
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def test_place_inherits_from_base_model(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_attributes(self):
        place_data = {
            "id": "101",
            "created_at": "2022-04-01T12:00:00.000000",
            "updated_at": "2022-04-02T12:00:00.000000",
            "city_id": "789",
            "name": "Cozy Cottage",
            "user_id": "123",
            "description": "A charming place to stay",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "amenity_ids": ["1", "2"]
        }
        place = Place(**place_data)

        self.assertEqual(place.id, "101")
        self.assertEqual(place.created_at, datetime.strptime("2022-04-01T12:00:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(place.updated_at, datetime.strptime("2022-04-02T12:00:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(place.city_id, "789")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.user_id, "123")
        self.assertEqual(place.description, "A charming place to stay")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["1", "2"])

    def test_save_method_updates_updated_at(self):
        place = Place()
        original_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(original_updated_at, place.updated_at)

    def test_to_dict_method_returns_dict(self):
        place = Place()
        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")

    def test_to_dict_method_contains_attributes(self):
        place = Place(city_id="456", name="Modern Apartment", user_id="789", description="Spacious and stylish",
                      number_rooms=3, number_bathrooms=2, max_guest=6, price_by_night=150,
                      latitude=34.0522, longitude=-118.2437, amenity_ids=["3", "4"])
        place_dict = place.to_dict()

        self.assertEqual(place_dict["city_id"], "456")
        self.assertEqual(place_dict["name"], "Modern Apartment")
        self.assertEqual(place_dict["user_id"], "789")
        self.assertEqual(place_dict["description"], "Spacious and stylish")
        self.assertEqual(place_dict["number_rooms"], 3)
        self.assertEqual(place_dict["number_bathrooms"], 2)
        self.assertEqual(place_dict["max_guest"], 6)
        self.assertEqual(place_dict["price_by_night"], 150)
        self.assertEqual(place_dict["latitude"], 34.0522)
        self.assertEqual(place_dict["longitude"], -118.2437)
        self.assertEqual(place_dict["amenity_ids"], ["3", "4"])

    def test_default_values_for_new_instance(self):
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_invalid_datetime_string_raises_exception(self):
        with self.assertRaises(ValueError):
            place_data = {"created_at": "invalid_datetime_string"}
            place = Place(**place_data)

    def test_updated_at_changes_after_save(self):
        place = Place()
        original_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(original_updated_at, place.updated_at)

if __name__ == "__main__":
    unittest.main()
