username = input("enter username:")
email = input("enter email:")
pwd = input("enter password:")
cpsw = input("confirm password:")

if len (username) > 0  and username .isalnum():
    if len (email) > 0 and '@' in email :
        if len(pwd) >= 5:
            if cpsw == pwd:
                print('registraion sucessfull')

            else:
                print('password does not match')
        else:
            print('password must be at leas 5 character')
    else:
        print('envalid email')
else :
    print ('envalid username')