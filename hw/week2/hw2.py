#4-6 Odd Numbers
odd_numbers = list(range(1,20,2))
for num in odd_numbers:
    print(num)
    
#4-8 Cubes
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

#4-9 Cube Comprehension
print([value**3 for value in range(1,11)])

#4-11 My Pizzas, Your Pizzas
fave_pizza = ['mushroom', 'olive', 'pineapple']
for pizza in fave_pizza:
    print("I like", pizza, "pizza.")
print("I really love pizza!")
friend_pizza = fave_pizza[:]
fave_pizza.append('tomato')
friend_pizza.append('pepper')
print("My favorite pizzas are:")
for pizza in fave_pizza:
    print(pizza)
print("My friend's favorites pizzas are:")
for pizza in friend_pizza:
    print(pizza)
    
#5-11 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num > 3:
        print(str(num)+"th")
    elif num == 3:
        print(str(num)+"rd")
    else:
        print(str(num)+"st")
    