x = input("enter a number:")
y = input("enter another number:")

if x.isnumeric():
    x = int(x)
else:
    print("setting of x to 0")
    x=0

if y.isnumeric():
    y = int(y)
else:
    print("setting y to 0")
    y = 0

z = x + y
print(f'total is {z}')