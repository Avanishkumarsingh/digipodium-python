name = "vijay deenanath chauhan"

m_name =name[6:15]
f_name =name[:5]
l_name =name[-7:]
print(m_name, f_name,l_name)


name = "Avanish Singh"
f_name =name[:8]
l_name =name[8:]
print(f_name)
print(l_name)
revname = name[::-1]
print(revname)
even_name = name[::2]
print(even_name)
odd_name = name[1::2]
print(odd_name)

message = '''
	
The New Mexico Territory was an organized incorporated territory of the United States from September 9, 1850, until  6, 1912. The territory was created from the U.S. provisional government of New Mexico, a result of Santa Fe de Nuevo México becoming part of the American frontier after the Treaty of Guadalupe Hidalgo.
'''
print("lenght of message is", len(message))
# first 100 char
print(message[:100])
# last 200 char
print(message[-200:])
#every 10 char
print(message[::10])
# all data expect first 100 char and last 100 char
print(message[100:-100])
