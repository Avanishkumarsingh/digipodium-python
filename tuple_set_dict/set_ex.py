a = {2,1,4,5}
b = {2,5,1,2,5,1,2,5,2,3,5,1,3,5,5,3,4,1}
print(a)
print(b)

# list to set
c = [1,5,3,2,1,12,21,3,5,2,3,3,5]
cs = set(c)
print(c)
print(set)

# empty set
d = set()
print(d)
d.add('Appleseed')
d.add('Banana')
d.add('Pine Apple')
d.add('Custerd Apple')
d.add('Apple')
print(d)
d.discard('Apple') # the better way to remove an item
print(d)
d.remove('Banana') # the dangerous way to remove the item
print(d)
d.clear()
print(d)