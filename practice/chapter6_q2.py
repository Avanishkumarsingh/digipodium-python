sub1 = int(input("Mark of sub1:"))
sub2 = int(input("Mark of sub2:"))
sub3 = int(input("Mark of sub3:"))

if (sub1+sub2+sub3)/3 < 33:
    print("failled in subject")
elif (sub1+sub2+sub3)/3 < 40:
    print("pass in subject")
else:
    print("Go to next class")