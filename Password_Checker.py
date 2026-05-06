import string
# more than 8 char
# one uppercase
# one lowercase
# one special
# one number

while True:
    password= input("Enter Password ")
    missing=[]
    stren=0

    if len(password) >=8:
        stren+=1
    else:
        missing.append("Password should be more than 8 characters ")
    
    if any(char in string.ascii_uppercase for char in password):
        stren+=1
    else:
        missing.append("Password should include atleast one Uppercase letter ")

    if any(char in string.ascii_lowercase for char in password):
        stren+=1
    else:
        missing.append("Password should include atleast one lowercase letter ")

    if any(char in string.punctuation for char in password):
        stren+=1
    else:
        missing.append("Password should include atleast one Special character ")

    if any(char in string.digits for char in password):
        stren+=1
    else:
        missing.append("Password should include atleast one number ")

    if(stren==5):
        print("Strong Password ")
        break

    else:
        for reasons in missing:
            print("-",reasons)
        print("/n Try again. ")
            
    