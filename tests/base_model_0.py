# base_model_0.py

"""Test BaseModel: save()"""

import unittest
from models.base_model import BaseModel


class TestBaseModelSave(unittest.TestCase):
    """Test cases for BaseModel save() method."""

    def test_save(self):
        """Test that save() method saves the BaseModel instance."""
        model = BaseModel()
        model.save()
        # Assert that the BaseModel instance is saved
        self.assertIsNotNone(model.updated_at)  # Ensure updated_at attribute is set after save()


if __name__ == '__main__':
    unittest.main()