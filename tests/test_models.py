# tests/test_models.py

import unittest
from models import Product  # assume Product model already defined

class TestProductModel(unittest.TestCase):
    
    def setUp(self):
        # Step 0: Fake product create karna
        self.product = Product(name="Test Product", category="Test Cat", available=True)
    
    # Step 1: READ test case
    def test_read_product(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.category, "Test Cat")
        self.assertTrue(self.product.available)
    
    # Step 2: UPDATE test case
    def test_update_product(self):
        self.product.name = "Updated Product Name"
        self.assertEqual(self.product.name, "Updated Product Name")
    
    # Step 3: DELETE test case
    def test_delete_product(self):
        del self.product
        with self.assertRaises(UnboundLocalError):
            print(self.product)
    
    # Step 4: LIST ALL test case
    def test_list_all_products(self):
        product2 = Product(name="Another Product", category="Test Cat", available=True)
        all_products = [self.product, product2]
        self.assertEqual(len(all_products), 2)
    
    # Step 5: FIND BY NAME test case
    def test_find_by_name(self):
        all_products = [self.product]
        result = [p for p in all_products if p.name == "Test Product"]
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Test Product")
    
    # Step 6: FIND BY CATEGORY test case
    def test_find_by_category(self):
        all_products = [self.product]
        result = [p for p in all_products if p.category == "Test Cat"]
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].category, "Test Cat")
    
    # Step 7: FIND BY AVAILABILITY test case
    def test_find_by_availability(self):
        all_products = [self.product]
        result = [p for p in all_products if p.available]
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0].available)

if __name__ == "__main__":
    unittest.main()

