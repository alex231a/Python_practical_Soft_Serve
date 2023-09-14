# Create a Pizza class with the attributes order_number
# and ingredients (which is given as a list).
# Only the ingredients will be given as input.
# You should also make it so that its possible to choose a ready made pizza flavour
# rather than typing out the ingredients manually!
# As well as creating this Pizza class, hard-code the following pizza flavours.

class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        Pizza.order_number += 1
        self.order_number = Pizza.order_number
        self.ingredients = ingredients

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])


p1 = Pizza(["bacon", "parmesan", "ham"])
print(p1.ingredients)
print(p1.order_number)

p2 = Pizza(["bacon2", "parmesan2", "ham2"])
print(p2.ingredients)
print(p2.order_number)


p3 = Pizza.garden_feast()
print(p3.ingredients)
print(p3.order_number)


print(p1.order_number)
print(p2.order_number)
print(p3.order_number)