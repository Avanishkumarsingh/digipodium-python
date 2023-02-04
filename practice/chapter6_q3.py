spam = ("Make a lot money","buy now","subscribe this","click this."'in comment')
for i in spam:
    msg = input("Enter a spam:")
if msg == i:
    print("spam detected")
else:
    print("spam not detected")