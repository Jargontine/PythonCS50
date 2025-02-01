menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def calculate_total(order):
    total = sum(menu[item] for item in order)
    return total

def display_order(order):
    total = calculate_total(order)
    print(f"Total: ${total:.2f}")

def place_order():
    order = []
    print("Welcome to Felipe’s Taqueria! Place your order:")

    while True:
        try:
            item = input("Enter an item (or press Ctrl-D to finish): ").title()
            if not item:
                break  

            if item in menu:
                order.append(item)
                display_order(order)
            else:
                print("Invalid item. Please choose from the menu.")

        except EOFError:
            break
if __name__ == "__main__":
    place_order()
