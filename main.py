

from models import Category, Product, CartItem, Bill


categories = []

products = []

user_cart = []

bills=[]


def display_user_menu():
    print("\nUser Menu:")
    print("1. View Categories")
    print("2. View Products by Category")
    print("3. View Product Details")
    print("4. Add to Cart")
    print("5. View Cart")
    print("6. Buy Products")
    print("7. Remove from Cart")
    print("8. Exit")

def view_categories():
    print("Categories:")
    for category in categories:
        print(f"{category.category_id}. {category.name}")




def view_products_by_category():
    print("\nCategories:")
    for category in categories:
        print(f"{category.category_id}. {category.name}")

    category_choice = int(input("\nEnter the category number to view products: "))

    selected_category = None
    for category in categories:
        if category.category_id == category_choice:
            selected_category = category
            break

    if selected_category is not None:
        print(f"\nProducts under {selected_category.name}:")
        for product in products:
            if product.category == selected_category:
                print(f"{product.product_id}. {product.name} - Rs. {product.price}")
    else:
        print("Invalid category choice.")


def view_product_details():
    print("\nProducts:")
    for product in products:
        print(f"{product.product_id}. {product.name}")

    product_choice = int(input("\nEnter the product number to view details: "))

    selected_product = None
    for product in products:
        if product.product_id == product_choice:
            selected_product = product
            break

    if selected_product is not None:
        print(f"\nProduct Details:")
        print(f"Name: {selected_product.name}")
        print(f"Price: Rs. {selected_product.price}")
        print(f"Category: {selected_product.category.name}")
        print(f"Description: {selected_product.description}")
    else:
        print("Invalid product choice.")

def add_to_cart():
    print("\nProducts:")
    for product in products:
        print(f"{product.product_id}. {product.name}")

    product_choice = int(input("\nEnter the product number to add to cart: "))

    selected_product = None
    for product in products:
        if product.product_id == product_choice:
            selected_product = product
            break

    if selected_product is not None:
        quantity = int(input("Enter the quantity to add: "))
        if quantity > 0:
            cart_item = CartItem(selected_product, quantity)
            user_cart.append(cart_item)
            print(f"{quantity} {selected_product.name}(s) added to cart.")
        else:
            print("Invalid quantity. Please enter a positive number.")
    else:
        print("Invalid product choice.")

def view_cart():
    if not user_cart:
        print("Your cart is empty.")
        return

    print("Your Cart:")
    total_amount = 0

    for cart_item in user_cart:
        product = cart_item.product
        quantity = cart_item.quantity
        subtotal = product.price * quantity

        print(f"{product.name} - Quantity: {quantity} - Subtotal: Rs. {subtotal}")
        total_amount += subtotal

    print(f"Total Cart Amount: Rs. {total_amount}")


    
def calculate_bill(cart_items):
    total_amount = 0

    for cart_item in cart_items:
        product = cart_item.product
        quantity = cart_item.quantity
        total_amount += product.price * quantity

    return total_amount

def apply_discount(total_amount):
    if total_amount > 10000:
        return total_amount - 500
    else:
        return total_amount

def buy_products():
    if not user_cart:
        print("Your cart is empty.")
        return

    total_amount = calculate_bill(user_cart)
    discount_amount = total_amount - apply_discount(total_amount)

    print("Bill Details:")
    print(f"Total Amount: Rs. {total_amount}")
    print(f"Discount: Rs. {discount_amount}")
    print(f"Final Amount to Pay: Rs. {total_amount - discount_amount}")

    print("Payment successful. Thank you for shopping!")
    user_cart.clear()

def remove_from_cart():
    if not user_cart:
        print("Your cart is empty.")
        return

    print("Your Cart:")
    for idx, cart_item in enumerate(user_cart, 1):
        product = cart_item.product
        quantity = cart_item.quantity
        print(f"{idx}. {product.name} - Quantity: {quantity}")

    choice = int(input("Enter the item number to remove: "))

    if 1 <= choice <= len(user_cart):
        del user_cart[choice - 1]
        print("Item removed from cart.")
    else:
        print("Invalid item choice.")


def add_category():
    category_id = int(input("Enter the category ID: "))
    name = input("Enter the category name: ")
    category = Category(category_id, name)
    categories.append(category)
    print(f"Category '{name}' added successfully.")

def add_product():
    if not categories:
        print("Please add categories first before adding products.")
        return

    print("Select a category for the product:")
    for category in categories:
        print(f"{category.category_id}. {category.name}")

    category_id = int(input("Enter the category ID: "))
    selected_category = None
    for category in categories:
        if category.category_id == category_id:
            selected_category = category
            break

    if selected_category is not None:
        product_id = int(input("Enter the product ID: "))
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        description = input("Enter the product description: ")

        product = Product(product_id, name, price, selected_category, description)
        products.append(product)
        print(f"Product '{name}' added to category '{selected_category.name}' successfully.")
    else:
        print("Invalid category ID.")

def view_products():
    print("Products:")
    for product in products:
        print(f"{product.product_id}. {product.name} - Rs. {product.price} - Category: {product.category.name}")

def view_bills():
    if not bills:
        print("No bills generated yet.")
        return

    print("Bills:")
    for bill in bills:
        print(f"Bill ID: {bill.id}")
        print("Items:")
        for cart_item in bill.items:
            product = cart_item.product
            quantity = cart_item.quantity
            subtotal = product.price * quantity
            print(f"{product.name} - Quantity: {quantity} - Subtotal: Rs. {subtotal}")

        print(f"Actual Amount: Rs. {bill.actual_amount}")
        print(f"Discount: Rs. {bill.discount}")
        print(f"Final Amount: Rs. {bill.final_amount}")
        print("-" * 30)





def user_flow():
    while True:
        print("\nWelcome to MyCart!")
        print("1. View Categories")
        print("2. View Products by Category")
        print("3. View Product Details")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Buy Products")
        print("7. Remove from Cart")
        print("8. Exit")

        choice = int(input("Enter your choice: "))


        if choice == 1:
            view_categories()
        elif choice == 2:
            view_products_by_category()
        elif choice == 3:
            view_product_details()
        elif choice == 4:
            add_to_cart()
        elif choice == 5:
            view_cart()
        elif choice == 6:
            buy_products()
        elif choice == 7:
            remove_from_cart()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")




def admin_flow():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Category")
        print("2. Add Product")
        print("3. View Products")
        print("4. View Bills")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_category()
        elif choice == 2:
            add_product()
        elif choice == 3:
            view_products()
        elif choice == 4:
            view_bills()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")




def main():
    categories.extend([
        Category(1, "Electronics"),
        Category(2, "Clothing"),
        Category(3, "Books"),
        Category(4, "Home & Kitchen"),
        Category(5, "Toys & Games"),
        Category(6, "Beauty & Personal Care"),
        Category(7, "Sports & Fitness")
    ])

    products.extend([
        Product(1, "Laptop", 50000, categories[0], "A powerful laptop."),
        Product(2, "T-Shirt", 1000, categories[1], "A comfortable T-shirt."),
        Product(3, "Python Book", 500, categories[2], "A book for Python enthusiasts."),
        Product(4, "Blender", 3000, categories[3], "A high-speed blender."),
        Product(5, "Building Blocks", 800, categories[4], "Educational building blocks."),
        Product(6, "Shampoo", 200, categories[5], "Nourishing shampoo."),
        Product(7, "Yoga Mat", 600, categories[6], "Comfortable yoga mat.")
    ])

    while True:
        print("\nWelcome to MyCart!")
        print("1. User Flow")
        print("2. Admin Flow")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_flow()
        elif choice == 2:
            admin_flow()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()








