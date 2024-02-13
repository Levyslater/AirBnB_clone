import unittest
from models.city import City
from datetime import datetime
import models
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def test_city_inherits_from_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        city_data = {
            "name": "New York",
            "state_id": "NY"
        }
        city = City(**city_data)

        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, "NY")

    def test_save_method_updates_updated_at(self):
        city = City()
        original_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(original_updated_at, city.updated_at)

    def test_to_dict_method_returns_dict(self):
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_to_dict_method_contains_attributes(self):
        city = City(name="Los Angeles", state_id="CA")
        city_dict = city.to_dict()

        self.assertEqual(city_dict["name"], "Los Angeles")
        self.assertEqual(city_dict["state_id"], "CA")

    def test_default_values_for_new_instance(self):
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_invalid_datetime_string_raises_exception(self):
        with self.assertRaises(ValueError):
            city_data = {"created_at": "invalid_datetime_string"}
            city = City(**city_data)

    def test_updated_at_changes_after_save(self):
        city = City()
        original_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(original_updated_at, city.updated_at)

if __name__ == "__main__":
    unittest.main()
