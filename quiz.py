ques = "what is the capital of india?"
oA = "A. Delhi"
oB = "B. Mumbai"
oC = "C. kolkata"
oD = "D. chennai"
correct = 'A'

print("Welcome to quiz")
print(ques)
print('-' * 10)
print(f'a) {oA}')
print(f'b) {oB}')
print(f'c) {oC}')
print(f'd) {oD}')
print ('-' * 20)

ans = input ('enter your answer:')
if ans =='A' or ans == 'a':
    print('correct ✅')
else:
    print('Incorrect❌')