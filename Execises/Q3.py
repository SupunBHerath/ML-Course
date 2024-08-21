list = ["Somapala","Gunapala","Siriapala"]
print(list)
op = input("Do you want to Add or Remove ( + / -) : ")
if(op == "+"): 
    newName = input("Enter a new name : ") 
    if( newName in list ):
        print(newName, "is already in the list : ")
        exit()
    else:
        list.append(newName)
        print(list)
        
elif(op == "-"):
    newName = input("Who do you want remove : " ) 
    if( newName in list ):
        list.remove(newName)
        print(list)
       
    else:
       print(newName, "name is already exists ")
       exit()
        
else:
    print("Invalid Option")
    exit()    
    

