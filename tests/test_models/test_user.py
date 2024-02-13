import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel 


class TestUser(unittest.TestCase):
    def test_user_inherits_from_base_model(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        user_data = {
            "email": "test@example.com",
            "password": "secure_password",
            "first_name": "John",
            "last_name": "Doe"
        }
        user = User(**user_data)

        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "secure_password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_save_method_updates_updated_at(self):
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(original_updated_at, user.updated_at)

    def test_to_dict_method_returns_dict(self):
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")

    def test_to_dict_method_contains_attributes(self):
        user = User(email="test@example.com", password="secure_password", first_name="John", last_name="Doe")
        user_dict = user.to_dict()

        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "secure_password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_default_values_for_new_instance(self):
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_invalid_datetime_string_raises_exception(self):
        with self.assertRaises(ValueError):
            user_data = {"created_at": "invalid_datetime_string"}
            user = User(**user_data)

    def test_updated_at_changes_after_save(self):
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(original_updated_at, user.updated_at)

if __name__ == "__main__":
    unittest.main()