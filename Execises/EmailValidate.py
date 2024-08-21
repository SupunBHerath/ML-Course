
email = input("Enter your email address : ")
# @gmail.com
if email[-10:]  == '@gmail.com' or email[-10:]  == '@yahoo.com':
    if email.islower() and not email.isdigit() and len(email)>10:
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        if len(password) >8 and not password.isalnum() :
            repassword = input("Enter your password again : ")
            if password == repassword:
                print("Registration Successful!")
            else:
                print("Passwords do not match!")  
        else:
         print("Password should be at least 8 characters & special characters ")  
            
    else:
     print("Invalid email address.")     
else:
    print("Invalid email address. Please use a gmail.com email address.")