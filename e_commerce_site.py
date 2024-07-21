import sys

products = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Smartphone", "price": 60000},
    {"id": 3, "name": "Headphones", "price": 15000},
    {"id": 4, "name": "Tablet", "price": 52000},
    {"id": 5, "name": "Smartwatch", "price": 30000}
]

cart = []

def display_products():
    print("\nAvailable Products:\n")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ₹{product['price']}")

def add_to_cart(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        cart.append(product)
        print(f"\nProduct '{product['name']}' added to cart.")
    else:
        print("\nProduct not found.")

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        total = 0
        for item in cart:
            print(f"\nName: {item['name']}, Price: ₹{item['price']}")
            total += item['price']
        print(f"\nTotal: ₹{total}")


def checkout():
    global cart
    if not cart:
        print("\nYour cart is empty. Add some items before checking out.")
        return

    print("\nCheckout Summary:")
    view_cart()
    total = sum(item['price'] for item in cart)
    print(f"\nTotal Amount to be Paid: ₹{total}")

    while True:
        payment_method = input("Enter payment method (Credit Card, Debit Card, Paytm, Google Pay, PhonePe etc.): ").strip().lower()
        if payment_method in ['credit card', 'debit Card', 'paytm', 'google Pay', 'phonepe']:
            print(f"\nPayment successful using {payment_method}. Thank you for shopping with us!")
            cart = []  
            break
        else:
            print("Invalid payment method. Please enter a valid payment method.")

def main():
    print("\n\nWelcome to Dhariya's E-commerce Site")
    while True:
        print("\nMenu:")
        print("1. Display Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_products()
        elif choice == '2':
            product_id = int(input("Enter product ID to add to cart: ").strip())
            add_to_cart(product_id)
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            print("\nThank you for using our e-commerce site. Goodbye!😀😀")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
