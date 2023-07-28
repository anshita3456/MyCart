
class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

class Product:
    def __init__(self, product_id, name, price, category, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.description = description

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Bill:
    def __init__(self, items, actual_amount, discount, final_amount):
        self.items = items
        self.actual_amount = actual_amount
        self.discount = discount
        self.final_amount = final_amount
