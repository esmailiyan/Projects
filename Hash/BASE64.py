from base64 import *

while 1:
    x=input("You want to 'ENcode' or 'DEcode' or 'EXit'?\n")
    x=x.lower()
    if x=='en':
        ans = b64encode(input("Enter: ").encode('utf-8')).decode()
        print('----------------------------------')
        print(ans)
        print('----------------------------------')
    elif x == 'de':
        try:
            ans = b64decode(input("Enter: ")).decode()
            print('----------------------------------')
            print(ans)
            print('----------------------------------')
        except:
            print("Couldn't decode!")
    elif x=='ex':
        exit(0)
    else:
        print('Try again !!')
