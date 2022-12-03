# convart month in a numbers if days


month = ("january","june","august","july","september","deover")
for i in month:
  if i =="february":
    print("the month of februar has 28/29 days")
  elif i in("january","march","may","july","august","october","december"):
    print("the month of 'i' has 31 days")
  elif i in ("april","june","september","november"):
    print("the month of 'i'has 30 days")
  else:
    print("this is not a valid month name")