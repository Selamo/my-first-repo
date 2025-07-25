#Repetition
# laugh = "ha" * 7
# print(laugh)

#message lenght
message = "Hello, Python!"
# print(len(message))

#accessing individual characters
first_letter = message[0]  #using positive indexing since we always start at 0 which is the first value
last_letter = message[-1]  #using negative indexing since we start from-1 which is always the last value
print(f"The first letter is {first_letter}")
print(f"The last letter is {last_letter}")

# #string formatting
# name = "Allino"
# age = 30
# score = 95.5

# #method 0ne f-string (Recommended)
# print(f"Hello, {name}! you are {age} years old.")
# print(f"Your score is {score:.1f}%")

# #method two: .format{} method
# print("Hello, {}! You are {} years old." .format(name, age))

# #method three: % formatting (older style)
# print("Hello, %s! You are %d years old." % (name, age))

# #String Methods: Python strings come with built-in methods
# text = " Hello, Python World! "

# #Case change
# print(text.upper())  #Converts all letters in text to caps
# print(text.lower())  #Converts all letters in text to lower case
# print(text.title())  #Capitalises the first letter of each word

# #Cleaning up
# print(text.strip())  #Removes unnecessary spaces like space at the end of text
# print(text.replace("Python", "Amazing Python")) #Replaces Python with Amazing Python

# #Checking content
# print(text.startswith("Hello"))  #False because text starts with a space 
# print(text.strip().startswith("Hello")) #True 
# print("Python" in text) #True

# #Splitting and joining
# words = "apple,banana,cherry".split(",")
# print(words)   #splits it to ['apple', 'banana', 'cherry,]
# joined = "-".join(words)
# print(joined)   #"apple-banana-cherry"

# #String Examples
email = input("enter your email")
if "@" in email and "." in email:
    username = email.split("@")[0]
    domain = email.split("@")[1]
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email format")

# # #Text analyser
# text = "The quick brown fox jumps over the lazy dog"
# print(f"Text: {text}")
# print(f"Length: {len(text)} characters ")
# print(f"words: {len(text.split())} words")
# print(f"Uppercase: {text.upper()}")
# print(f"Lowercase: {text.lower()}")
# print(f"Title case: {text.title()}")
# print(f"Contains 'fox': {'fox' in text}")


# # #Exercises for string
# # #1.
# #Name formatting. get a  name input and output it such that the name is the first letters of each name is in caps then, the first and last name

# name = input("Enter your name: ")

# print(f"Your name is {name.title()}")
# print(f"First name = {name.split()[0]} \n Last name = {name.split(" ")[1]}") 

# #2.
# #Word counter
# #count how many words, characters and how many times a appears

# sentence = "Python is an amazing programming language"
# print(f"Characters: {len(sentence)}")
# print(f"Words: {len(sentence.split())}")
# print(f"number of a's in sentence: {sentence.count('a')}")