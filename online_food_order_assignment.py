# Simple Online Food Ordering System

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        print("\nYour Order:")
        for item in self.items:
            print(f"- {item.name} : ₹{item.price}")
        print(f"Total: ₹{self.calculate_total()}")

class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, menu):
        print(f"\nWelcome {self.name}! Here is the menu:")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ₹{item.price}")

        while True:
            choice = input("Enter item number to add (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(menu):
                self.order.add_item(menu[int(choice) - 1])
                print(f"{menu[int(choice) - 1].name} added to your order.")
            else:
                print("Invalid choice, try again.")

        self.order.show_order()


# Example usage
menu = [
    FoodItem("Pizza", 250),
    FoodItem("Burger", 150),
    FoodItem("Pasta", 200),
    FoodItem("Sandwich", 100),
    FoodItem("Coffee", 80)
]

customer_name = input("Enter your name: ")
customer = Customer(customer_name)
customer.place_order(menu)