# tests/test_models.py

import unittest
from models import Product  # assume Product model already defined

class TestProductModel(unittest.TestCase):
    
    def setUp(self):
        # fake product create karna
        self.product = Product(name="Test Product", category="Test Cat", available=True)
    
    def test_read_product(self):
        # product ka data read karna
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.category, "Test Cat")
        self.assertTrue(self.product.available)

if __name__ == "__main__":
    unittest.main()
