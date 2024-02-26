# base_model_4.py

"""Test BaseModel: __str__ method"""

import unittest
from models.base_model import BaseModel


class TestBaseModelStr(unittest.TestCase):
    """Test cases for BaseModel __str__ method."""

    def test_str(self):
        """Test that __str__ method returns a string representation."""
        model = BaseModel()
        str_repr = str(model)
        # Assert the content of the string representation
        self.assertIsInstance(str_repr, str)  # Ensure __str__ method returns a string


if __name__ == '__main__':
    unittest.main()