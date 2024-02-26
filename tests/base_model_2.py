# base_model_2.py

"""Test BaseModel: self.id"""

import unittest
from models.base_model import BaseModel


class TestBaseModelId(unittest.TestCase):
    """Test cases for BaseModel id attribute."""

    def test_id(self):
        """Test that id attribute is unique."""
        model1 = BaseModel()
        model2 = BaseModel()
        # Assert that id attribute is unique for each instance
        self.assertNotEqual(model1.id, model2.id)


if __name__ == '__main__':
    unittest.main()