# # Read through the comments to understad variables
# print("Hello, Deepseeds")

# #why we need variables: for code reusability
# #Variables arre memory locations
# name =  "Allen"

# print("I am Gita, I love the name -Gita, it was given to me by my father, Paul Gita and I really like the name Gita.")

# print("I am " + name + ", I love the name -" + name + ", it was given ti me by my father, " + name + "Paul")

# #A vairiable
# #is a string if it is inside of single or double quotes
# name =  "Allen"
# #is a number and can be float(decimal) or integer(whole  number)
# age = 23 #integer
# height = 3.56 #float
# #is a boolean if it can either be true or false/ 0 or 1
# #this is a boolean
# isMarried = True
# #or it can be false

# #naming convention
#2name = "John"
#324my-name = "John"
#Snake casing: always use snake casing in python
user_name = "Peter"
#camel casing: It works but not the naming convention
userName = "Peter"
#Pascal casing: It works but not the naming convetion
UserNameFrom = "Paul"
#naming using keywords is not correct as variable names for example using words like class, string etc. Keywords are prebuilt words in Python

#Variables basic examples
#Numbers
whole_number = 42  #integer(int)
decimal_number = 3.14159  #float
complex_number = 2 + 3j   #complex

#Text
greeting = "Heloo,World!"  #string (str)
single_char = "A"   #Also a string

#Boolean (TreuFalse)
is_sunny = True  #Boolean
is_raining = False

#Check the rype of any variable
print(type(greeting))   #<class 'str">
print(type(complex_number))  #<class 'complex'>

#Concatenate variables

#Personal Information
first_name = "Emma"
last_name = "Watson"

#This is not addition  because we are adding two strings. This is called concatenation.
full_name = first_name +" " + last_name

#string formatter called f-string. Helps format the print statement
print(f"Hello, {full_name}!")

