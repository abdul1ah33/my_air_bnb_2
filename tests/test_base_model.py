import unittest
from models.base_model import BaseModel
'''
'''
class TestBaseModel(unittest.TestCase):
    def test_init(self):

        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
    
    def test_save(self):

        my_model = BaseModel()
        int_created_at = my_model.created_at
        final_date = my_model.save()
        self.assertNotEqual(int_created_at, final_date)

    def test_to_dict(self):
        my_model = BaseModel()
        dictionary = my_model.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary["id"], my_model.id)
        self.assertEqual(dictionary["created_at"], my_model.created_at.isoformat())
        self.assertEqual(dictionary["updated_at"], my_model.updated_at.isoformat())
        self.assertEqual(dictionary["__class__"], "BaseModel")

    def test_str(self):
        """
        Test for string representation
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == "__main__":
    unittest.main()