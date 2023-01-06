x = (1,2,3) # tuple
y = 2,5,7,2 # tuple packing
print(x)
print(y)
print(type(x))
print(type(y))
print(x[0]) # index 0
print(x[1]) # index 1
print(y[-1]) # index -1
z = (1,2,3,4,5,6,7,8,9,10)
print(z[:5]) # slicing

# tuple method - count, index
a = ('Apple','Apple','Apple','Banana','Pine Apple','Custerd Apple')
print(f'len of is{len(a)}')
print(f'Apple occures {a.count("Apple")}times')
print(f'Pine Apple occures{a.count("Pine Apple")}times')
print(f'Banana is at index {a.index("Banana")}')

# tuple to list
z1 = list(z)
print(type(z), type(z1))
print(z,z1)

# list to tuple
z2 = tuple(z1)
print(type(z2), type(z1))
print(z1, z2)

# single item tuple
s = (1,) # comma is important
s2 = 2, # is also tuple
print(type(s))
print(type(s2))