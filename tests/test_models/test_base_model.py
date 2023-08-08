#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from uuid import uuid4
import datetime


class TestBaseModel(unittest.TestCase):
    def test_has_atrributes(self):
        # Test attributes after instantiation
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"), True)
        self.assertTrue(hasattr(base_model, "created_at"), True)
        self.assertTrue(hasattr(base_model, "updated_at"), True)
        
    def test_id_is_a_string(self):
        # Test if ID is a string
        base_model = BaseModel()
        self.assertTrue(type(base_model.id) == str, True)
        self.assertEqual(type(base_model.id) == int, False)
        self.assertEqual(type(base_model.id), str)
        
    def test_id_is_unique(self):
        # Test if ID is unique
        base_model =  BaseModel()
        self.assertEqual(base_model.id == uuid4(), False)
        
    def test_unique_id(self):
        # Test two instances don't have the same ID
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)
    
    def test_created_is_datetime(self):
        # Test created_at attribute is an instance of datetime
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime.datetime)
    
    def test_created_is_datetime(self):
        # Test updated_at attribute is an instance of datetime
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime.datetime)
        
    def test_to_dict_method(self):
        # Test to_dict() method returns a dict
        base_model = BaseModel()
        base_dict = base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        
    def test_save_method(self):
        # Test save() method updates updated_at
        base_model = BaseModel()
        initial_val = base_model.updated_at
        base_model.save()
        updated_val = base_model.updated_at
        self.assertNotEqual(initial_val, updated_val)
        
    def test_str_method(self):
        # Test __str__ method
        instance = BaseModel()
        expected_format = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(instance.__str__(), expected_format)
        

if __name__ == '__main__':
    unittest.main()