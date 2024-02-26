# base_model_1.py

"""Test BaseModel: to_dict()"""

import unittest
from models.base_model import BaseModel


class TestBaseModelToDict(unittest.TestCase):
    """Test cases for BaseModel to_dict() method."""

    def test_to_dict(self):
        """Test that to_dict() method returns a dictionary representation."""
        model = BaseModel()
        model_dict = model.to_dict()
        # Assert the content of the dictionary representation
        self.assertIsInstance(model_dict, dict)  # Ensure to_dict() returns a dictionary


if __name__ == '__main__':
    unittest.main()