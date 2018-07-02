
# Ex 4d

class MyClass():
    def __init__(self, val):
        self.val = 5

    def print_things(self, val):
        print(self.val == val)
        print("self.val: " + str(self.val))
        print("val: " + str(val))

val = 3
my_class_obj = MyClass(val)
my_class_obj.print_things(7)
