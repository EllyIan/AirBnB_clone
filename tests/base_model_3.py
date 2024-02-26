# base_model_3.py

"""Test BaseModel: self.created_at"""

import unittest
from models.base_model import BaseModel


class TestBaseModelCreatedAt(unittest.TestCase):
    """Test cases for BaseModel created_at attribute."""

    def test_created_at(self):
        """Test that created_at attribute is set correctly."""
        model = BaseModel()
        # Assert that created_at attribute is set when an instance is created
        self.assertIsNotNone(model.created_at)


if __name__ == '__main__':
    unittest.main()