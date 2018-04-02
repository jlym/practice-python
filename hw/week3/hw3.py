# 6-5: Rivers
rivers = {
    'nile': 'egypt',
    'euphrates': 'iraq',
    'seine': 'france'}

for river, country in rivers.items():
    print('The ' + river.title() + ' in ' + country.title() + ' is prone to flooding.')

print("The notable rivers are:")
for river in rivers.keys():
    print(river.title())

print("Countries with notable rivers are:")
for country in rivers.values():
    print(country.title())
    
#6-8: Pets
spot = {
    'dog': 'bob',
    'guinea pig': 'susan',
    'cat': 'penelope'
}

rover = {
    'dog': 'dan',
    'hamster': 'jack',
    'fish': 'carol'
}

bunny = {
    'rabbit': 'john',
    'dog': 'sarah',
    'parrot': 'amanda'
}

pets = [spot, rover, bunny]

for pet in pets:
    print(pet)
