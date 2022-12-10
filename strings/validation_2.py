a = input("Enter a number:")
b = input("Enter another number:")
if a.isnumeric() and b.isnumeric():
    a,b = int(a),int(b)
    c= a+b
    print("The sum of number is:", c)
else:
    print("Enter number only")


a =input("Enter a number:")
b =input("Enter another number:")
if a.isnumeric() and b.isnumeric():
    a,b = int(a),int(b)
    c =a+b
    print("The sum of number is:", c)
else:
    print("Enter number only")