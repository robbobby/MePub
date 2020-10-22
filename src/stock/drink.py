class Drink:
    def __init__(self, name, units, price,):
        self.price = price
        self.units = units
        self.name = name

    def is_alchoholic(self):
        return self.units > 0