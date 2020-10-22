class Customer:
    def __init__(self, name, age, hunger, thirst, drunk_level, naughty_level):
        self.naughty_level = naughty_level
        self.drunk_level = drunk_level
        self.thirst = thirst
        self.hunger = hunger
        self.name = name
        self.age = age

    def is_over_18(self):
        return self.age >= 18

