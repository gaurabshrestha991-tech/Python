cart = []

while True:
    print("\nShopping Cart")
    
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Calculate total")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        
        cart.append((item, price))
        print("Item added to cart.")
        
    elif choice == "2":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nItems in cart:")
            for item, price in cart:
                print(item, "-", price)
                
    elif choice == "3":
        item = input("Enter item name to remove: ")
        
        found = False
        
        for product in cart:
            if product[0] == item:
                cart.remove(product)
                found = True
                print("Item removed")
                break
        if not found:
            print("Item not found")
            
    elif choice == "4":
        total = 0
        
        for item, price in cart:
            total += price
        print("Total price: ", total)
        
    elif choice == "5":
        print("ThankYou for shopping!")
        break
    else:
        print("Invalid choice.")
