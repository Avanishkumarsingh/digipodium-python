# Creating a dictionary

a = {'Name':'Zara','Age':7,'Class':'First'}
# getting all the key from the dictionary
print(a.keys()) # use list(a.keys()) to display at list

# getting all the values from the dictionary
print(a.values())

# gettng all the items from the dictionary as a list of tuples
print(a.items())

# nested dictionary
b = {
    'fruits':{'apple':'5 kg','custard apple':'3 kg',},
    'vegetables':{'cabbage':'1 pc','tomato':'500 gm'},
    'cereals':{'rice':'1 kg','wheat':'2 kg'}}
from pprint import pp
pp(b)
print(b)
print("keys of b=>",b.keys())
print("values of b=>", b.values())

# accessing a value from a dict.
print(a['Name'])
print(a['Class'])
# priint(a['city']) # keyError: 'city'

# accessing a value from a dict using get()
print(a.get('Name'))
print(a.get('Age'))
print(a.get('Class'))
print(a.get('city')) # None
print(a.get('city', 'Not Found')) # default value can be specified
print(a.get('Name', 'Not Found'))

# traversing a dict
# style 1
for key in a:
    print(key, a[key])

# style 2
for key, value in a.items():
    print(key, value)

# only values
for value in a.values():
    print(value)