username = input('enter user name:')
email = input('enetr email:')
pwd = input('enter password:')
cpwd = input('confirm password:')

if len(username) > 0 and username.isalnum():
    if len(email) > 0 and '@' in email:
        if len(pwd)>=4:
            if pwd == cpwd:
                print('registration successful')
            else:
                print('password do not match')
        else:
             print('password must be at least 4 character')
    else:
        print('invalid email')
else:
    print('username is invalid')
