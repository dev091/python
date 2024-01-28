#used to store data in key value pair
#curly braces used {}

marks = {'hindi': 90 , 'maths':75 , 'physics':85}
print(marks)
print(type(marks))
print(marks['hindi']) # finding marks of hindi
print(marks.get('hindi')) #finding marks thru get function
print(marks.get('bio')) #not available so return none

marks['bio'] =78 # adding new variable
print(marks) 

del marks['maths']
print(marks) # delt maths marks

marks[0] = {'information systems': 90}
print(marks)