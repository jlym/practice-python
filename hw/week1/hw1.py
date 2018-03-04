"""Exercise 2.4"""
print()
print("Exercise 2-4")
name = 'wackie jackie'
print(name.upper())
print(name.lower())
print(name.title())

#Exercise 2.7
print()
print("Exercise 2-7")
name2 = ' \t wackie jackie \n'
print(name2)
print(name2.rstrip()) #how come this doesnt remove the tab at the front?
print(name2.lstrip())
print(name2.strip())

#Exercise 2.9
print()
print("Exercise 2-9")
fave_number = 14
print("My favorite number is", str(fave_number)+"!")

#Exercise 3.3
print()
print("Exercise 3-3")
fave_transport = ['lapras', 'sharpedo', 'gyarados', 'swampert']
print("I like to ride", fave_transport[0].title(), "to the PokeCenter.")
print("It's much better to ride", fave_transport[-1].title(), "to work than taking the Bart.")
print(fave_transport[1].title(), "is handy because he can break sea boulders and swim very quickly.")

#Exercise 3.4-3.7, 3.9
print()
print("Exercise 3-4 to 3-7 and 3-9")
guests = ['Kukui', 'Birch', 'Elm', 'Oak']
for guest in guests:
    print(guest+", you are invited to a dinner of berries at 7 PM on Saturday.")
print(guests[-1]+" can't make it")
guests[-1] = 'Juniper'
for guest in guests:
    print(guest+", you're invited to a dinner of berries at 7 PM on Saturday.")
guests.insert(0, 'Sycamore')
guests.insert(3, 'Rowan')
guests.append('Ivy')
for guest in guests:
    print(guest, ", you're invited to a grand dinner of berries at 7 PM on Saturday.")
print("I can only invite two people for dinner.")

while len(guests) >2: 
    uninvited = guests.pop()
    print("Sorry, ", uninvited+", dinner is cancelled.")
print(guests[0], "you're invited to an intimate dinner of berries at 7 PM on Saturday.")
print(guests[1], "you're invited to an intimate dinner of berries at 7 PM on Saturday.")
print(len(guests), "guests are coming to dinner. They are:", guests)
del guests[:]
print(guests)

#Exercise 3.8
print()
print("Exercise 3-8")
places = ['Junto', 'Kanto', 'Hoenn', 'Alola']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
