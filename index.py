
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

#While loop = execute some code While some condition remains true

# name= input("Enter your name:")

# while name == "":
#   print("you did not enter your name")
#   name= input("Enter your name:")
#   print(f"Hello {name}")

# age= int(input("Enter your age:"))

# while age < 0:
#     print("Age can be less than 0")
#     age= int(input("Enter your age:"))
   
# print(f"Your are {age} years old")


#Logical operators = evaluate multiple condtions ( or , and, not)
#  or = at least one condtion must be true 
#  and = both condtions must be true
#  not = inverts the condition (not false, not True)

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter another food you like (q to quit): ")
    
# print("bye")

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f" Your number is {num}")   

#python compound interest calculator

priciple = 0
rate = 0
time = 0

# while priciple <= 0:
#     priciple = float(input("Enter the principal amount: "))
#     if priciple <= 0:
#         print("Principal must be greater than 0")


# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate must be greater than 0")

# while time <= 0:
#     time = int(input("Enter the time period in years: "))
#     if time <= 0:
#         print("Time period must be greater than 0")


# while True:
#     priciple = float(input("Enter the principal amount: "))
#     if priciple < 0:
#         print("Principal must be less than 0")
#     else:
#         break


# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate must be less than 0")
#     else:
#         break

# while True:
#     time = int(input("Enter the time period in years: "))
#     if time < 0:
#         print("Time period must be less than 0")
#     else:
#         break

# total = priciple * pow((1 + (rate / 100)), time)
# print(f"Balance after {time} years/s : ${total:.2f}")


# for loop = execute some code for each item in a sequence (list, string, range,etc)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)


# Countdown timer

import time

# my_time = int(input("Enter the time in seconds:"))

# for x in range(0, my_time):
#     print(x)
#     time.sleep(1)

# print("Time's up!") 

# my_time = int(input("Enter the time in seconds:"))

# for x in reversed(range(0, my_time)):
#     print(x)
#     time.sleep(1)

# print("Time's up!") 


# my_time = int(input("Enter the time in seconds:"))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02} second remaining")
#     time.sleep(1)

# print("Time's up!") 

# nested Loops= a loop within another loop ( outer loop and inner loop)


# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#     for y in range (columns):
#         print(symbol, end="")
#     print()


# Collection = single "Variable" used to store multiple values (List, Tuple, Set, Dictionary)
# List = []ordered, changeable, allows duplicate values
# Set = {} unordered, immutable, but  Add/ Remove OK, no duplicate values
# Tuple = () ordered, unchangeable, allows duplicate values


# fruits = ["apple", "banana", "orange", "grape", "mango"]

# print(dir(fruits))
# print(help(fruits))

# print(fruits[0:3])

# for fruit in fruits:
#     print(fruit)
# print(len(fruits))

# print("apple" in fruits)
# print("kiwi" in fruits)

# fruits[0] = "kiwi"

# for fruit in fruits:
#  print(fruit)

# fruits.append("banana")
# print(fruits)


# fruits.remove("orange")


# fruits.insert(0, "kiwi")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("grape"))
# print(fruits.count("grape"))
# print(fruits)



#### Set ={} unordered, immutable, but  Add/ Remove OK, no duplicate values


# fruits = {"apple", "banana", "orange", "grape", "mango", "apple"}
# # print(dir(fruits))

# # fruits.add("kiwi")
# # fruits.remove("orange")
# # fruits.pop()
# # fruits.clear()


# print(fruits)


# Tuple = () ordered, unchangeable, allows duplicate values

# fruits = ("apple", "banana", "orange", "grape", "mango")
# # print(dir(fruits))


# # fruits.count("apple")
# # print(fruits.index("apple"))
# # fruits.remove("apple")
# # fruits.append("kiwi")
# # fruits.sort()
# # fruits.reverse()
# # fruits.clear()
# # print(len(fruits))
# print(fruits)

# Shopping cart program using list, set and tuple

# foods = []
# prices =[]
# total = 0

# while True:
#     food = input("Enter a food to add to your cart (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of the {food}: $"))
#         foods.append(food)
#         prices.append(price)
 
        

# print("-----Your Shopping Cart-----")

# for food in foods:
#     print(food, end=" ")
   


# for price in prices: 
#     total = total + price 
# print()
# print(f"Your total is: ${total}")  

# 2dlist = [list1, List2, List3]
 


# grocery_List = [["apple", "banana", "orange"],
#                 ["carrot", "broccoli", "spinach"],
#                   ["chicken", "pork", "lamb", "fish"]]


# for collection in grocery_List:
#     for food in collection:
#         print(food, end=" ")
#     print()


# num_pad = ((1, 2, 3,), 
#            (4, 5, 6,), 
#            (7, 8, 9,), 
#            ("*", 0, "#"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()


# Python quiz game 

# questions = (("What is the capital of France?"),
#               ("What is the largest planet in our solar system?"),
#               ("What is the chemical symbol for gold?"),
#               ("Who wrote 'Romeo and Juliet'?"),
#               ("What is the tallest mammal?"))

# options = (("a) Paris", "b) London", "c) Rome", "d) Berlin"),
#            ("a) Earth", "b) Jupiter", "c) Mars", "d) Saturn"),
#            ("a) Ag", "b) Au", "c) Gd", "d) Pt"),
#            ("a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain"),
#            ("a) Elephant", "b) Giraffe", "c) Blue Whale", "d) Hippopotamus"))


# answers = ("a", "b", "b", "b", "c")
# guesses = []
# score = 0
# question_num = 0


# for question in questions:
#     print("----------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter your answer (a, b, c, d): ").lower()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("Correct!")
#     else:
#         print("Incorrect!")
#         print(f"The correct answer is: {answers[question_num]}")


#     question_num += 1


# print("------------------")
# print("    Results       ")
# print("------------------")


# print("answers: ", end=" ")
# for answer in answers:
#     print(answer, end=" ")
# print()


# print("guesses: ", end=" ")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")



# Dictionary = {} unordered, changeable, indexed by key, no duplicate keys

# capitals = {"USA": "Washington D.C.",
#             "France": "Paris",
#             "Japan": "Tokyo",
#             "India": "New Delhi",}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Singapore"))


# if capitals.get("Japan"):
#     print("The Capital exists!")
# else:
#     print("The Capital does not exist!")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"Spain": "Madrid"})

# capitals.pop("India")
# capitals.popitem()
# capitals.clear()


# keys = capitals.keys()
# for key in keys:
#     print(key, end=" ")


# values = capitals.values()

# for value in capitals.values():
#     print(value, end=" ")

# items = capitals.items()

# for key, value in capitals.items():
#      print(f"{key}: {value}")

# Concession stand program using dictionary

# menu = {"beer": 2.50,
#                "wine": 3.50,
#                "chocolate": 1.50,
#                "vodka": 1.00,
#                "beer and wine": 3.00,
#                 "chocolate and vodka": 2.00,
#                 "beer and chocolate": 3.00,
#                 "wine and vodka": 4.00,
#                  "beer and vodka": 3.50,
#                  "wine and chocolate": 4.00
#                 }
               
# cart = []
# total = 0


# print("------------------- MENU ---------------------------")
# for key, value in menu.items():
#     print(f"{key:20}: ${value:.2f}")
# print("----------------------------------------------------")


# while True:
#     food = input("Enter a food to add to your cart (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
        
# print("------------------- Your Order ----------------------")
# for food in cart:
#     # total = total + menu.get(food)
#     total += menu.get(food)
#     print(food, end=" ")
    
    
# print()
# print(f"Your total is: ${total:.2f}")