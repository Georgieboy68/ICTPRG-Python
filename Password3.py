Username1='Bob'
Username2='fred'
Username3='lock'
Password1='1234'
Password2='happyPass122'
Password3='passwithlock44'
Username=input('Enter your Username: ')
Password=input('Enter your Password: ')
if Username==Username1 and Password==Password1:
    print ('Access is granted:')
elif Username==Username2 and Password==Password2:
    print ('Access is granted:')
elif Username==Username3 and Password==Password3:
    print ('Access is granted:')
else:
    print('Password is incorrect')