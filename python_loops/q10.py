# Q10. Shopping cart menu
# Use while True to show a menu: 1. Add item, 2. View cart, 3. Checkout.
# Add item: ask for the name and price, and store them in a dictionary
# View cart: print every item and the total
# Checkout: print the total; if it is over Rs 5000, give 10% off. Then break


view_cart = {}
total = 0

while True:
    print("\n1. Add item")
    print("2. View cart")
    print("3. Checkout")

    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter item name: ")
        price = int(input("Enter the price: "))

        view_cart[item_name] = price
        total += price

        print("Item added successfully!")

    elif choice == "2":
        print("\nYour Shopping Cart:")

        for item, price in view_cart.items():
            print(item, "=", price)

        print("Total:", total)

    elif choice == "3":
        print("\nCheckout")

        if total > 5000:
            discount = total * 0.10
            final_total = total - discount
            print("Original Total:", total)
            print("Discount:", discount)
            print("Final Total:", final_total)
        else:
            print("Total:", total)
            print("No discount available.")

        break

    else:
        print("Invalid choice! Try again.")
