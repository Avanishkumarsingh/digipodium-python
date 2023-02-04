s = { }
s.update ({"Zaid":"Digipodium"})
s.update({"Aditya":"Data Analystic"})
s.update({"Udbhav":"My SQL"})
s.update({"Avanish":"Data Sciencetist"})
print(s)

# adding 
lang = {}
for i in range(1,5):
    name = input("Enter your name:")
    language = input("Enter your favourite language:")
    lang.update({name:language})
print(lang)