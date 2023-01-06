#1 write a python program to create a tuple.
x = tuple()
print(x)

#2 write a python program to create tuple with different data type.
items =("price",'3rs','7rs')
print(items)

#3 to create a tuple with numbers and print one items.
tuplex = (22,45,92,100,83)
print(tuplex)
tuplex = (92)
print(tuplex)

#4 to unpack a tuple in several variables.
x = (5,9,4)
print(x)
a1,a2,a3 = (x)
print (a1+a2+a3)

#5 write a python program to add an item in a tuple.
tuplex = (4,37,98,9)
print(tuplex)
tuplex = tuplex + (5,)
print(tuplex)
tuplex = tuplex [:3] + (10, 45,66) + tuplex[:3]
print(tuplex)

#6 write a python program to convert a tuple to a string
tup = ('4','5','8','10')
str = ' '. join(tup)
print(str)

#7 write a python program to get the 4th element and 4th element from last of a tuple.
tuplex = ('x','g','h','o','r','e','i','p','f')
print(tuplex)
item = tuplex[3]
print(item)
item1 = tuplex[-4]
print(item1)

#8 write a python program to create the colon of a tuple.


#9 write a python program to find the repeated items of a tuple.
tuplex = (1,5,7,5,6,3,8,2,4,9,6,5,3,3,4,2,4,)
print(tuplex)
count = tuplex.count(4)
count1 = tuplex.count(3)
print(count)
print(count1)

#10 wrrite a python program to check whether an element axists within a tuple.
tuplex = ('e','y','u','r','f','h',5,2,'c',)
print("u"in tuplex)
print(3 in tuplex)

#11 write a python program to convert a list to a tuple.
listx = [2,6,4,8,9]
print(listx)
tuplex = tuple(listx)
print(tuplex)

#12 write a python program to remove an item from a tuple.
tuplex = ('a','g','r','w','k','r')
print (tuplex)
listx = list(tuplex)
listx.remove("g")
print(listx)