import unittest
from main import calculate_bill, apply_discount
from models import Category, Product, CartItem, Bill

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category(1, "Electronics")
        self.assertEqual(category.category_id, 1)
        self.assertEqual(category.name, "Electronics")

    def test_category_name(self):
        category = Category(2, "Clothing")
        self.assertEqual(category.name, "Clothing")

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        category = Category(1, "Electronics")
        product = Product(1, "Laptop", 50000, category, "A powerful laptop.")
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 50000)
        self.assertEqual(product.category, category)
        self.assertEqual(product.description, "A powerful laptop.")

    def test_product_price(self):
        category = Category(2, "Clothing")
        product = Product(2, "T-Shirt", 1000, category, "A comfortable T-shirt.")
        self.assertEqual(product.price, 1000)

class TestCartItem(unittest.TestCase):
    def test_cart_item_initialization(self):
        category = Category(1, "Electronics")
        product = Product(1, "Laptop", 50000, category, "A powerful laptop.")
        cart_item = CartItem(product, 2)
        self.assertEqual(cart_item.product, product)
        self.assertEqual(cart_item.quantity, 2)
   
    def test_cart_item_quantity(self):
        category = Category(2, "Clothing")
        product = Product(2, "T-Shirt", 1000, category, "A comfortable T-shirt.")
        cart_item = CartItem(product, 0)
        self.assertEqual(cart_item.quantity, 0)

class TestBill(unittest.TestCase):
    def test_bill_initialization(self):
        category = Category(1, "Electronics")
        product = Product(1, "Laptop", 50000, category, "A powerful laptop.")
        cart_item = CartItem(product, 2)
        items = [cart_item]
        bill = Bill(items, 100000, 500, 99500)
        self.assertEqual(bill.items, items)
        self.assertEqual(bill.actual_amount, 100000)
        self.assertEqual(bill.discount, 500)
        self.assertEqual(bill.final_amount, 99500)

    def test_bill_discount(self):
        category = Category(2, "Clothing")
        product = Product(2, "T-Shirt", 500, category, "A comfortable T-shirt.")
        cart_item = CartItem(product, 5)
        items = [cart_item]
        bill = Bill(items, 2500, 0, 2500)
        self.assertEqual(bill.discount, 0)

class TestFunctions(unittest.TestCase):
    def test_calculate_bill(self):
        category = Category(1, "Electronics")
        product1 = Product(1, "Laptop", 50000, category, "A powerful laptop.")
        product2 = Product(2, "Phone", 20000, category, "A high-end phone.")
        user_cart = [CartItem(product1, 2), CartItem(product2, 1)]
        self.assertEqual(calculate_bill(user_cart), 120000)

    def test_apply_discount(self):
        discount_1 = apply_discount(10000)
        discount_2 = apply_discount(20000)
        print(f"Discount 1: {discount_1}, Expected: 10000")
        print(f"Discount 2: {discount_2}, Expected: 19500")
        self.assertEqual(discount_1, 10000)  
        self.assertEqual(discount_2, 19500)  

if __name__ == "__main__":
    unittest.main()
