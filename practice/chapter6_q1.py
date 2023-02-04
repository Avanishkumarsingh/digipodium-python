num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
num4 = int(input("Enter a number:"))

if (num1 > num2 and num1 > num4):
    print("1's is greater")
elif (num2 > num3):
    print("2's num is greater")
elif (num3 > num4):
    print("3's num is grater")
elif (num4 > num2):
    print("4's is grater")
else:
    print("done")