class Counter():
    def __init__(self, name):
        self.name = name
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

    def __repr__(self):
        """Returns a string representation of this object that should
        be printed"""
        return self.name + ": " + str(self.count)

red_cars = Counter('red cars')
blue_cars = Counter('blue cars')

red_cars.increment()
blue_cars.increment()
red_cars.increment()
blue_cars.increment()
red_cars.increment()

# When we print a counter object, __repr__ is first called, which returns
# the string that should be printed
print(red_cars)
print(blue_cars)
