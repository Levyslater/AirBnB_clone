import unittest
from models.state import State
from datetime import datetime
import models
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Main class"""
    def test_state_inherits_from_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        """Sample State class attributes"""
        state_data = {
            "name": "California"
        }
        state = State(**state_data)

        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)
        self.assertEqual(state.name, "California")

    def test_save_method_updates_updated_at(self):
        """Test save method on updated at attribute"""
        state = State()
        original_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(original_updated_at, state.updated_at)

    def test_to_dict_method_returns_dict(self):
        """Test to_dict method"""
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")

    def test_to_dict_method_contains_attributes(self):
        """Test to_dict method"""
        state = State(name="New York")
        state_dict = state.to_dict()

        self.assertEqual(state_dict["name"], "New York")

    def test_default_values_for_new_instance(self):
        """Test default object attributes"""
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.name, "")

    def test_invalid_datetime_string_raises_exception(self):
        """Test invalid datetime string"""
        with self.assertRaises(ValueError):
            state_data = {"created_at": "invalid_datetime_string"}
            state = State(**state_data)

    def test_updated_at_changes_after_save(self):
        """Test updated at changes after save"""
        state = State()
        original_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(original_updated_at, state.updated_at)

if __name__ == "__main__":
    unittest.main()
