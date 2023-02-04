x = [] # empty list
# 
x.append(2)
x.append(5)
print(x)
x.append(10)
print(x)
for i in range(11,17):
    x.append(i)
print(x)
y = [23,54,45]
x.append(y)
print(x)
x.extend(y) # it will add the last 
print(x)
x.insert(2,9)
print(x)
x.insert(10,"hello") #string at index 10
x.insert(18,[2,5,1,5]) # list insert at index 18
print(x)