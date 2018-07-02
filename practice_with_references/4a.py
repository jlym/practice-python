# 4 Classes

# Objects created from classes are also mutable

# Ex 4a

class Circle():
    def __init__(self, radius):
        self.radius = radius

a = Circle(2)
b = a

# What gets printed?
print(a.radius)
print(b.radius)

# Do a and b reference the same object, or different objects?
print(a is b)
