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
#user_name = "Peter"
#camel casing: It works but not the naming convention
#userName = "Peter"
#Pascal casing: It works but not the naming convetion
#UserNameFrom = "Paul"
#naming using keywords is not correct as variable names for example using words like class, string etc. Keywords are prebuilt words in Python

#Variables basic examples
#Numbers
# whole_number = 42  #integer(int)
# decimal_number = 3.14159  #float
# complex_number = 2 + 3j   #complex

# #Text
# greeting = "Heloo,World!"  #string (str)
# single_char = "A"   #Also a string

# #Boolean (TreuFalse)
# is_sunny = True  #Boolean
# is_raining = False

# #Check the rype of any variable
# print(type(greeting))   #<class 'str">
# print(type(complex_number))  #<class 'complex'>

# #Concatenate variables

# #Personal Information
# first_name = "Emma"
# last_name = "Watson"

# #This is not addition  because we are adding two strings. This is called concatenation.
# full_name = first_name +" " + last_name

# #string formatter called f-string. Helps format the print statement
# print(f"Hello, {full_name}!")

#Exercise 1. 
# A ban name generator

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
age = input("How old are you? ")
school = input("Which school do you attend?: ")
department = input("Which department? ")
best_friend = input("What is your best friend's name?: ")
fav_meal = input("What is your favourite meal?: ")
tribe = input("What is your tribe?: ")
region = input("Which region?: ")
sport = input("Which sport do you love")

print(f"My name is {full_name}, I am {age} years old. I school in{school}, in the department of{department}.My best freind name is{best_friend}.My favourite meal is {fav_meal}.I am from {tribe} in the {region} region.I love playing{sport}")


#Exercise 2.
# #Create a calculator for a rectangle.

length = int(input("Enter length of rectangle: "))
width = int(input("Enter the rectangle's width: "))

perimeter = 2 * (length + width)
area = length * width
print(f"The Area of the rectabgle with length {length} and width {width} is {area}\n It's Perimeter = {perimeter}")

#Exercise 3.
#Temperature Converter; Convert from Celsius to Fahrenheit

temp_in_celsius = float(input("Enter temperature in celsius: "))
temp_in_fahrenheit = (temp_in_celsius * (9/5)) + 32
print(f"{temp_in_celsius} degree celsius in Fahrenheit is {temp_in_fahrenheit} degree Fahrenheit")

#Exercise 4. 
#Swap variacles put. like if a is 5 and b is 6, the output should be the resverse.

a = int(input("Enter first num ber to be swapped: "))
b = int(input("Enter second number for swapping: "))

print(f"The value entered for a = {a} and for b = {b}")
#assign the value of a to temp
temp = a
#assign the value of b to a
a = b
#assign the value of temp (which was the former value of a) to b
b = temp

print(f"After swap, a = {a}\n b = {b}")