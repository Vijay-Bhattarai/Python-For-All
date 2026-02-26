
# #this are strings
# first_name = "Bhattarai"
# food = "I like Pizza"
# email= "bijaybhattrarai5544@gmail.com"

# print(f"Vijay {first_name}")
# print(f"Hey Man, {food}")
# print(f"hey its my email you can contact directly from here- {email}")


# #Integers 
# age = 26

# print(f"you are {age} years old.")

# #float 
# price = 7.99 

# print(f"the price is {price}")


# #Boolean

# is_student = True


# # #TypeCasting
# # person_name = "vijay"
# # age = 26
# # gpa = 3.40
# # is_student = True


# # person_name = bool(person_name)

# # print(person_name)

# # #input 
# # person_name= input("What is your name: ")
# # age = int(input("How old are you ?: "))

# # # age = int(age)
# # age = age + 1 

# # print(f"its good name {person_name}")
# # print(" Happy Birthday!")
# # print(f"Your are {age} Years old.")
 
#Calucate 

# Length = float(input(" Enter the length: "))
# Width = float(input(" Enter the Width: "))

# Area = Length * Width 

# print( f" The Area is : {Area} cm ") 

#Shopping Cart Program 

# item = input("What item Would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many Would you like?: "))
# total = price * quantity

# print(f"you have total bought {quantity}  x {item}/s")
# print(f"your total is: ${total}")


# Madlibs Game
# Word Game where you create a story 
# By filling in blanks with random words

# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing':")
# adjective3 = input("Enter an adjective (description): ")


# print(f"Today i went to a {adjective1} zoo.")
# print(f" In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")


# Arthmetic Operators
# friends = 10
# friends = friends + 1 
# friends += 1
# friends = friends - 1
# friends -= 1
# friends  = friends * 3
# friends *= 3
# friends = friends / 2

# friends /= 2

# friends = friends ** 2
# friends **=2

# remainder = friends % 3

# print(remainder)


# Math Function 

# x = 3.14
# y = 2
# z= 5


# result = round(x)
# result = abs(y)
# result = pow(4, 3)
# result = max(x, y, z)
# result = min(x, y, z)


# print(result)


# import math

# x = 9.9

# # print(math.pi)
# # print(math.e)

# # result = math.sqrt(x)
# # result = math.ceil(x)
# result = math.floor(x)

# print(result)

# import math


# radius = float(input('Enter the radius of a circle: '))


# circumference = 2 * math.pi * radius
# area = math.pi * radius ** 2

# print(f"The circumference is: {round(circumference, 2)}cm")
 

# if - Do some code only if some condtion is True 
#     Else do something else 


# age = int(input("Enter your age: "))

# if age >= 120:
#     print("You cannot vote!")
# elif age >= 18:
#     print("You are old enough to vote!")
# elif age < 0:
#     print("Please enter a valid age!")

# else:
#     print("You are too young to vote!")


# response = input("Do you like Python? (yes/no):")

# if response == "yes":
#     print("Great! I love Python too!")
# else:
#     print("Okay, maybe another time.")

# name = input("Enter your name:")

# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")

# for_sale = False

# if for_sale:
#     print("Item is for sale!")
# else:
#     print( "Item is not for sale!")

# # Python calculator
# operator = input("Enter an operator (+, -, *, /): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter Second number: "))

# if operator == "+":
#     result = num1 + num2
#     print (round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print (round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print (round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print (round(result, 3)) 
# else:
#     print(f"{operator} is not a valid operator")


 # Python weight conveter Program 

# weight = float(input("Enter your weight: "))
# unit = input("Killograms or Pounds?( K or `L): ")


# if unit == "K":
#     weight =  weight * 2.205
#     unit = "lbs."
#     print(f"Your weight is {round(weight)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "kgs."
#     print(f"Your weight is {round(weight)} {unit}")
# else:
#     print(f"{unit} is not valid")
    
# Logical operators = evaluate mutliple comdtions ( or , and, not)
#   or = at least one condtion must be true 
#   and = both condtions must be true
#   not = inverts the condition (not false, not True)

# temp = 20
# is_raining = True


# if temp > 35 or temp < 0 or is_raining:
#     print("It's not a good time to go outside!")
# else:
#     print("It's a good time to go outside!")
 
# temp = 0
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print(" It is hot outside!")
#     print(" It is sunny")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside")
#     print("It is sunny")
# elif  28 > temp > 0 and is_sunny:
#     print("It is warm outside")
#     print("It is sunny")
# elif temp <= 0 and not is_sunny:
#     print("It is cold outside")
#     print("It is Cloudy")
# elif  28 > temp > 0 and not is_sunny:
#     print("It is warm outside")
#     print("It is Cloudy")
# elif  28 > temp > 0 and not is_sunny:
#     print("It is warm outside")
#     print("It is Cloudy")

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#  print or assign one of two values based on a condition 
#  X if condition else Y 

# num = 7
# a = 6
# b = 7 
# age = 17
# tempertature = 16
# user_role = "Guest"
# # print("Postive" if num> 0 else "Negative")
# # result = "Even" if num % 2 == 0 else "0dd"
# # max_num = a if a > b else b
# # min_num = a if a < b else b
# # status = "Adult" if age >= 18 else "Child"
# # weather = "Hot" if tempertature > 20 else "Cold"

# access_level = "Full Acess" if user_role == "Admin" else "Limited Acess"

# print(access_level)

# string methods 

# name = input("Enter your full name: ")

# phone_number = input("Enter your phone number: ")

# result = name.find("a")
# result = name.rfind("l")
# result = len(name)
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")

# print(phone_number)


# print(help(str))


#Validate user input exercise 
#1. usenname is no more than  12 characters
#2. username must not contain spaces
#.  username must be not contain digits 

# username = input("Enter a username: ")



# if len(username) > 12:
#     print("Your username can't be more than 12 character" )
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces ")
# elif  not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}")


#String Indexing = acessing elements of a sequence using [] (indexing operator ) 
# # [start : end : step]

# credit_number = "1333-3343-3433-3432"

# # print(credit_number[0])
# # print(credit_number[0:4])
# # print(credit_number[5:9])
# # print(credit_number[5:])
# # print(credit_number[-1])
# # print(credit_number[::2])

# credit_number = credit_number[::-1]

# # last_digits = credit_number[-4:]
# # print(f"xxxx-xxxx-xxxx-{last_digits}")

# print(credit_number) 

#Format specifiers = {value.flags} format a value based on what flags are inserted

# price1 = 233234.34324
# price2 = -324324.324
# price3 = 1233.34

# print(f"Price is ${price1:+,.2f}")
# print(f"Price is ${price2:+,.2f}")
# print(f"Price is ${price3:+,.2f}")


