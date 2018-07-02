# Ex 4b 

class Circle():
    def __init__(self, radius):
        self.radius = radius

a = Circle(2)
b = Circle(2)

# Do a and b reference the same object, or different objects?
print(a is b)

print(a.radius)
print(b.radius)
