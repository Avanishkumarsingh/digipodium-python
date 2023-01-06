x = {1,2,3,4}
y = {3,4,5,6}
ans = x.union(y)
print(ans)

ans1 = x.intersection(y)
print(ans1)

ans2 = x.difference(y)
print(ans2)

x = {1,4,6,7,2,5}
y = {5,7,9,2,4,1}
print(x)
print(y)
print('union')
print(x|y) # same as x.union(y)
print('intersection')
print(x&y) # same as x.intersection(y)
print('difference')
print("unique values in x=>", x - y)# same as x.difference(y)
print("unique values in x=>", y - x)
print('symmetric difference')
print(x ^ y)# sabe as x.symmetric_difference(y)

z = {10,11,12,13}
print('disjoint set')
print("kya x or y me kuch common nahi h =>",x.isdisjoint(y))
print("kya x or z me kuch common nahi h =>",x.isdisjoint(z))
print("kya z or y me kuch common nahi h =>",z.isdisjoint(y))

items = {'apple','orange','banana','potato','tomato','brinjal'}
fruits = {'apple','orange','banana'}
vegetables = {'potato','tomato','brinjal','cucumber'}

print('subset')
print('fruits belong to item',fruits.issubset(items))
print('vegetables belong to item',vegetables.issubset(items))