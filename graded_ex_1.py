# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    return sorted_list



def display_products(products_list):
    print("Products available:")
    for idx, (product, price) in enumerate(products_list, start=1):
        print(f"{idx}. {product} - ${price}")



def display_categories():
    print("Categories available:")
    for idx, category in enumerate(products.keys(), start=1):
        print(f"{idx}. {category}")



def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))


def display_cart(cart):
    print("Your cart:")
    for idx, (product, quantity) in enumerate(cart, start=1):
        print(f"{idx}. {product} (x{quantity})")


def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Products purchased:")
    for product, quantity in cart:
        print(f"- {product}: {quantity}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")



def validate_name(name):
    parts = name.split()
    if len(parts) != 2 or not all(part.isalpha() for part in parts):
        return False
    return True

def validate_email(email):
    return "@" in email


def main():
    cart = []
    total_cost = 0
    
    # Ask user for their name
    while True:
        name = input("Enter your name (first and last): ")
        if validate_name(name):
            break
        print("Invalid name. Please provide both first and last names, only alphabets.")
    
    # Ask user for their email
    while True:
        email = input("Enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email with '@'.")
    
    # Show categories
    while True:
        display_categories()
        category_choice = input("Select a category by entering the corresponding number: ")
        
        if category_choice.isdigit():
            category_choice = int(category_choice)
            categories = list(products.keys())
            if 1 <= category_choice <= len(categories):
                category_name = categories[category_choice - 1]
                product_list = products[category_name]
                while True:
                    display_products(product_list)
                    
                    print("\nOptions:")
                    print("1. Select a product to buy")
                    print("2. Sort the products according to price")
                    print("3. Go back to the category selection")
                    print("4. Finish shopping")
                    option = input("Choose an option: ")
                    
                    if option == "1":
                        product_choice = input("Enter the product number: ")
                        if product_choice.isdigit() and 1 <= int(product_choice) <= len(product_list):
                            product_choice = int(product_choice) - 1
                            product, price = product_list[product_choice]
                            quantity = int(input(f"How many {product}s would you like to buy? "))
                            add_to_cart(cart, product, quantity)
                            total_cost += price * quantity
                        else:
                            print("Invalid product number.")
                    
                    elif option == "2":
                        sort_order = int(input("Enter 1 for ascending, 2 for descending order: "))
                        sorted_products = display_sorted_products(product_list, sort_order)
                        display_products(sorted_products)
                    
                    elif option == "3":
                        break  # Go back to categories
                    
                    elif option == "4":
                        if cart:
                            display_cart(cart)
                            address = input("Enter your delivery address: ")
                            generate_receipt(name, email, cart, total_cost, address)
                        else:
                            print("Thank you for using our portal. Hope you buy something next time!")
                        return  # End the shopping session
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid category number.")
        else:
            print("Please enter a valid number.")

    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
