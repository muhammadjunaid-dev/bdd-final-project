import unittest
from routes import get_product, update_product, delete_product, list_products  # assume routes exist

class TestRoutes(unittest.TestCase):

    def test_read_product(self):
        product = get_product(1)  # fake id
        self.assertEqual(product['name'], "Test Product")

    def test_update_product(self):
        product = update_product(1, {'name': 'Updated Product'})
        self.assertEqual(product['name'], 'Updated Product')

    def test_delete_product(self):
        result = delete_product(1)
        self.assertTrue(result)

    def test_list_all_products(self):
        products = list_products()
        self.assertTrue(len(products) > 0)

if __name__ == "__main__":
    unittest.main()
