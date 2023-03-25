set1 = {'Ram','Shyam','Jenny'}
set2 = {'Jenny','Jiya','Akash'}
set3 = {'Ankur','Pradeep'}
print(set1.union(set2,set3))# Union
#print(set1 | set2 |set3)
set1.update(['Jenny','Mohan'])
print(set1)
#set2.union(set1))

# Intersection
print(set1.intersection(set2,set3))
set1.intersection_update(set2)
print(set1)
print(set2)