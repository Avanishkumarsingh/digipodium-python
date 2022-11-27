import random

print("random number generator")
print('enter y to generate a new random')
while input('continue[y/n]:')=='y':
    number = random. randint(1000,9999)
    print(f'lucky number: {number}')
print("thanks for using")