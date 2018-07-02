# Ex 4c

class MyClass():
    def __init__(self, val):
        self.val = val

    def print_things(self, val):
        print(self.val == val)
        print("self.val: " + str(self.val))
        print("val: " + str(val))

val = 3
my_class_obj = MyClass(val)
my_class_obj.print_things(5)
