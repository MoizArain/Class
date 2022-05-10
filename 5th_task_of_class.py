# creat a class of name laptop with attributes of brand, model, price
# apply discount on the price
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def discount(self):
        self.price = self.price - (self.price * 0.2)

lap1 = Laptop("HP", "ProBook", 100000)
lap2 = Laptop("lenovo", "Thinkpad", 200000)
Lap3 = Laptop("Toshiba", "Satellite", 300000)
lap4 = Laptop("Dell", "XPS", 400000)

print(lap2.price)
lap2.discount()
print(lap2.price)