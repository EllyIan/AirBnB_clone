#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

# Test cases for the BaseModel class
class TestBaseModel(unittest.TestCase):

    # Test initialization of BaseModel
    def test_init(self):
        # Create a new BaseModel instance
        my_model = BaseModel()

        # Assert that the expected attributes are not None
        self.assertIsNotNone(my_model.id)  # Check for a unique ID
        self.assertIsNotNone(my_model.created_at)  # Check for creation timestamp
        self.assertIsNotNone(my_model.updated_at)  # Check for update timestamp

    # Test saving a BaseModel instance
    def test_save(self):
        # Create a new BaseModel instance
        my_model = BaseModel()

        # Store the initial updated_at timestamp
        initial_updated_at = my_model.updated_at

        # Call the save method
        my_model.save()

        # Assert that the updated_at timestamp has changed
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    # Test converting a BaseModel instance to a dictionary
    def test_to_dict(self):
        # Create a new BaseModel instance
        my_model = BaseModel()

        # Convert the instance to a dictionary
        my_model_dict = my_model.to_dict()

        # Assert that the result is a dictionary
        self.assertIsInstance(my_model_dict, dict)

        # Assert expected keys and values in the dictionary
        self.assertEqual(my_model_dict["__class__"], "BaseModel")  # Check class name
        self.assertEqual(my_model_dict["id"], my_model.id)  # Check ID
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())  # Check creation timestamp
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())  # Check update timestamp

    # Test the string representation of a BaseModel instance
    def test_str(self):
        # Create a new BaseModel instance
        my_model = BaseModel()

        # Assert that the string representation starts with "[BaseModel]"
        self.assertTrue(str(my_model).startswith("[BaseModel]"))

        # Assert that the ID and dictionary representation are included in the string
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

# Run the tests if this file is executed directly
if __name__ == "__main__":
    unittest.main()
