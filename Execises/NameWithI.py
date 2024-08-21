firstname=input('First name :' )
secoundName=input('Second name : ' )
lastname=input('Last name : ')

print(firstname[0]+'.'+ lastname[0]+'.', lastname)


number =input('Enter your Number : ')
ccode = input('Enter your country code : ')

if (len(number)==10) : 
    if(number[0]== '0'):
       
        print('your Telephone Number is  : ' ,ccode+number[1:]) 
    else:
        print("enter your valid number , firt character is must be a 0")
    
    
else:
    print("Enter your valid number")

