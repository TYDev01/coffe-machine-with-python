class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: int, quantity=0):
        # I used assertion statement to handle error when the inputted price or quantity is less than zero
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        self.name = name  # we assigned the attribute here dynamically, rather than repeating it while calling.
        self.price = price
        self.quantity = quantity
        # print(f"An instance created for: {name}")

    # To get the total of what we have we assign a method to our Class
    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.calculate_price() - self.pay_rate


item1 = Item("Phone", 2000, 2)
item2 = Item("Laptop", 300, 5)

print(f"We received {item1.quantity} {item1.name} at the price of {item1.price}, total is {item1.calculate_price()}.")
print(f"We received {item2.quantity} {item2.name} at the price of {item2.price}, total is {item2.calculate_price()}.")
print(Item.__dict__)
print(item1.__dict__)
