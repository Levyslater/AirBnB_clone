#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import io
import sys
import os

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass
    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    def test_attributes(self):
        self.assertEqual(self.my_model.name, "My_First_Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_id_generation(self):
        self.assertIsNotNone(self.my_model.id)

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_created_at_type(self):
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_to_dict_method(self):
        my_model_dict = self.my_model.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, my_model_dict)

        self.assertEqual(my_model_dict['id'], self.my_model.id)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_from_dict_method(self):
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(self.my_model.id, my_new_model.id)
        self.assertEqual(self.my_model.created_at, my_new_model.created_at)

    def test_identity(self):
        my_new_model = BaseModel(**self.my_model.to_dict())
        self.assertFalse(self.my_model is my_new_model)

if __name__ == '__main__':
    unittest.main()
