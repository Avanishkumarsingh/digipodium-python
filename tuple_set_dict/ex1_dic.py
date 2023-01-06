contacts = {'emergency': '112',
    'office': '983745'}
print(contacts)
while True:
    print("->call")
    print("->exit")
    print('-'*10)
    cnt = input("Do you want to call, exit or add:")
    if cnt == 'call':
        name = input("Enter name of contact:")
        if name in contacts:
            print(f'calling{name} at {contacts [name]}')
        else:
            print(f'{name} not found')
    elif cnt == 'exit':
        break
    elif cnt == 'add':
        name = input("Enter name of contacts:")
        number = input("Enter number of contacts:")
        contacts[name] = number
        print(f'{name} added successfully')
    else:
        print('Invalid choice')
    print('-'*10)