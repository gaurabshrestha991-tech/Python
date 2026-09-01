class ShoppingCart:
    def __init__(self):
        self.products = {}
        
    def add_product(self, name, price, quantity):
        self.products[name] = [price, quantity]
        
    def total_bill(self):
        total = 0
    
        for product in self.products.values():
            price = product[0]
            quantity = product[1]
            total += price * quantity
            
        return total
    
    def show_cart(self):
        for name, details in self.products.items():
            print(name, "Price:", details[0], "Quantity:", details[1])
            
cart = ShoppingCart()

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 1000, 2)
cart.add_product("KeyBoard", 2500, 1)

cart.show_cart()

print("Total Bill:", cart.total_bill()) 
