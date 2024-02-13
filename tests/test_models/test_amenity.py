import unittest
from models.amenity import Amenity
from datetime import datetime
import models
from models.base_model import BaseModel
class TestAmenity(unittest.TestCase):
    def test_amenity_inherits_from_base_model(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        amenity_data = {
            "id": "456",
            "created_at": "2022-02-01T12:00:00.000000",
            "updated_at": "2022-02-02T12:00:00.000000",
            "name": "Wifi"
        }
        amenity = Amenity(**amenity_data)

        self.assertEqual(amenity.id, "456")
        self.assertEqual(amenity.created_at, datetime.strptime("2022-02-01T12:00:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(amenity.updated_at, datetime.strptime("2022-02-02T12:00:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(amenity.name, "Wifi")

    def test_save_method_updates_updated_at(self):
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(original_updated_at, amenity.updated_at)

    def test_to_dict_method_returns_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_to_dict_method_contains_attributes(self):
        amenity = Amenity(name="Pool")
        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict["name"], "Pool")

    def test_default_values_for_new_instance(self):
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_invalid_datetime_string_raises_exception(self):
        with self.assertRaises(ValueError):
            amenity_data = {"created_at": "invalid_datetime_string"}
            amenity = Amenity(**amenity_data)

    def test_updated_at_changes_after_save(self):
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(original_updated_at, amenity.updated_at)

if __name__ == "__main__":
    unittest.main()
