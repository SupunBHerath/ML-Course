# ================================== Day 01 =================================================================

name = input('Enter your name : ') # get input
name = name.upper() # upper case
print('upper case :',name) # print
print('\nlowercase :',name.lower()) # print lower case
print('\n lengthx: ',len(name)) # print length
print('\n casfold : ', name.casefold()) # print casfold
print('\n swap : ', name.swapcase()) # print swap
print('\n',name[0].lower()) # print name in lower case
print('\n first letter capital ',name.capitalize()) # print name in 
print('\n last letter capital ',name.capitalize()) # print name
print('\n',name.lower().count('u'))
print('\n',name.count('U'))
print ('a' in name)
print ('a' not in  name)
print(name.find('A'))
print(name.index)