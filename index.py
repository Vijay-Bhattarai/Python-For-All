
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

from ast import While
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


# Random number
# low = 1
# high = 100
# options =("rock", "paper", "scissors")
# cards = ["2 of Hearts", "3 of Diamonds", "4 of Clubs", "5 of Spades", "6 of Hearts", "7 of Diamonds", "8 of Clubs", "9 of Spades", "10 of Hearts", "Jack of Diamonds", "Queen of Clubs", "King of Spades", "Ace of Hearts"]


# import random

# # number = random.randint(low, high)
# # number = random.random()
# # option = random.choice(options)

# random.shuffle(cards)
# print(cards)


# # python number guessing game
# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0 
# is_running = True

# print("Welcome to the Number Guessing Game!")
# print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")

# while is_running:
#     guess = input("Enter your guess: ")
    
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
        
#         if guess < lowest_num or guess > highest_num:
#             print(f"Invalid guess! Please select a number between {lowest_num} and {highest_num}.")
#         elif guess <answer:
#             print("Too low! Try again.")
#         elif guess > answer:
#             print("Too high! Try again.")
#         else:
#             print(f"Correct! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False

#     else:
#         print("Invalid guess!")
#         print(f" Please select a number between {lowest_num} and {highest_num}.")

# # Rock Paper Scissors Game
# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:
#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter rock, paper, or scissors: ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")


#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("Player wins!")
#     elif player == "paper" and computer == "rock":
#         print("Player wins!")
#     elif player == "scissors" and computer == "paper":
#         print("Player wins!")
#     else:
#         print("You lose!")
        
#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False
        
# print("Thanks for playing!")
      

#  dice roller program ⚂


# import random

# # ◦ ┌ ┐ └ ┘ ─ │

# "┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐"
# "│                   │"
# "│                   │"
# "│                   │"
# "└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘"


# dict_art = {
#     1:("┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐", 
#        "│                   │", 
#        "│          ◦        │", 
#        "│                   │", 
#        "└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘"),
#     2:("┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐", 
#        "│ ◦                 │", 
#        "│                   │", 
#        "│          ◦        │", 
#        "└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘"),
#     3:("┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐", 
#        "│  ◦                │", 
#        "│          ◦        │", 
#        "│                 ◦ │", 
#        "└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘"),
#     4:("┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐", 
#        "│  ◦                │", 
#        "│          ◦        │", 
#        "│      ◦          ◦ │", 
#        "└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘"),
#     5:("┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐",
#        "│  ◦     ◦          │",
#        "│  ◦      ◦         │",
#        "│                 ◦ │",
#        "└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘"),
#     6:("┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐",
#        "│  ◦     ◦          │",
#        "│  ◦      ◦         │",
#        "│  ◦              ◦ │",
#        "└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘")
     
# }


# dice = []
# total = 0 
# number_of_dice = int(input("Enter the number of dice to roll: "))

# for die in range(number_of_dice):
#     dice.append(random.randint(1, 6))
    
# # for die in range(number_of_dice):
# #    for line in dict_art.get(dice[die]):
# #       print(line)

# for line in range(5):
#    for die in dice:
#       print(dict_art.get(die)[line], end=" ")
#    print()

# for die in dice:
#       total = total + die
# print(f"Total: {total}")


# function = A block of resuable code
# place () after the function name to invoke it


# def  happy_new_year(Year, fname, lname):
#       print(f"Happy New Year {Year}, {fname} {lname} !")
#       print("Wishing you a year filled with joy and prosperity!")
#       print("May all your dreams come true in the coming year!")
#       print()

# happy_new_year(2083, "Vijay", "Bhattarai")

# def display_invoice(customer_name, amount, due_date):
#     print(f"Invoice for {customer_name}")
#     print(f"Amount Due: ${amount:.2f}")
#     print(f"Due Date: {due_date}")
    
# display_invoice("Vijay Bhattarai", 250.75, "2024-07-15")


# return = statement used to end a function and send a result back to the caller

# def add(x, y):
#    z= x + y
#    return z


# def subtract(x, y):
#    z= x - y
#    return z


# def multiply(x, y):
#    z= x * y
#    return z

# def divide(x, y):
#    z= x / y
#    return z

# print(add(5,3))
# print(subtract(5,3))
# print(multiply(5,3))
# print(divide(5,3))

# def create_name(first_name, last_name):
#      first_name = first_name.capitalize()
#      last_name= last_name.capitalize()
#      return first_name + " " + last_name

# full_name = create_name("vijay", "bhattarai")
# print(full_name)

# default agruements - A defults vaule is assigned to a parameter in the function definition.
# If the caller does not provide a value for that parameter, the default value will be used.
#  of argument 1. positional arguments 2. keyword arguments 3. default arguments 4. arbitrary arguments

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1-discount) * (1 + tax)

# print(net_price(100))
# print(net_price(500, 0.1))

# default arguments
# import time


# def count(end, start = 0):
#      for x in range(start, end +1):
#           print(x)
#           time.sleep(1)
#      print("Time's up!")
     
# count(30,15)

# keyword arguments = am argument that is passed to a function by name, rather than by position.
# keyword arguments are always passed after positional arguments.


# def hello(greeting, title, first, last):
#      print(f"{greeting}, {title} {first} {last}!")
     
# hello("Hello", title= "Mr.", last= "Bhattarai", first= "Vijay")


# for x in range (1, 11):
#      print(x, end="")

# def get_phone(county, area, first, last):
#      return f"{county}-{area}-{first}-{last}"

# phone_num = get_phone(county="97", area="949", first="555", last="1212")

# print(phone_num)

#arbitrary arguments
#*args = variable length argument list (allows you to pass mutiple non-key arguments)
#**kwargs = variable length keyword argument list( allows you to pass multiple keyword-arguments)
# * unpacking operator 


# def add(*args):
#      total = 0
#      for arg in args:
#        total += arg
#      return total


# print(add(1, 2, 3, 4, 5))

# def display_name(*args):
#      for arg in args:
#           print(arg, end=" ")

# display_name( "Mr.", " Vijay", "Bhattarai")


# def print_address(**kwargs):
#      for key, value in kwargs.items():
#           print(f"{key}: {value}")
     
# print_address(street="123 Main St", 
#               city="New York", 
#               state="NY",
#               zip="10001",
#               country="USA")

# agrs and kwargs 

# def shipping_label(*args, **kwargs):
#      for arg in args:
#           print(arg, end=" ")
#           print()
          
#      # for key, value in kwargs.items():
#      #      print(f"{key}: {value}", end=" ")
#      print(f"{kwargs.get('weight')} {kwargs.get('height')} {kwargs.get('length')} {kwargs.get('delivery_date')}")

# shipping_label("123 Main St", "New York", "NY", "10001", "USA", 
#                     weight=10, height=2, width=1, length=4, delivery_date="2024-07-15")


# Iteratables = An object/collection that can return its elements one at a time , allowing it to be iterated over.
# Iterables are objects that can be looped over using a for loop.
# Iterables include lists, tuples, sets, dictionaries, and strings.

# numbers = (1, 2, 3, 4, 5)

# for num in numbers:
#      print(num)


# fruits = {"apple", "banana", "cherry", "coconut"}

# for fruit in fruits:
#      print(fruit)

# name = "Vijay Bhattarai"

# for char in name:
#      print(char, end= " ")


# my_dict = {"name": "Vijay", "age": 25, "city": "New York"}

# for key, value in my_dict.items():
#      print(f"{key}: {value}")

# Membership Operators = used to test whatever a value or variable is found in a seqeunce
# (string, list, tuple, set or dictornary)
# 1. in
# 2. not in 


# word = "Apple"

# letter = input("Enter a  secret letter: ")


# if letter in word:
#       print(f"Congratulations! You found the letter {letter}")
# else:
#       print(f"Sorry, the secret letter is not in the {word}.")

# if letter not in word:
#        print(f"Sorry, the secret letter is not in the {word}.")
# else:
#     print(f"Congratulations! You found the letter {letter}")
    
# List Comprehesions = A concise way to create list in python 
# compact and easier to read than tradtional loops
# [Expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)] 

# print(squares)

# fruits = ["apple", "banana", "cherry", "coconut"]

# fruits = [fruit.upper() for fruit in fruits]
# fruits_chars = [fruit[0] for fruit in fruits]
# print(fruits_chars)

# numbers = [1,-2,3,-4,5,-6,7,-8,9,-10]
# postive_num = [ num for num in numbers if num >= 0] 
# negative_num = [ num for num in numbers if num <= 0] 
# even_num = [ num for num in numbers if num % 2 == 0 ] 
# odd_num = [ num for num in numbers if num % 2 == 1 ] 

# print(odd_num)

# Match-case-statement (switch): An aternative to using many 'elif' statement
# Execute some code if a value matches a 'case'
# Benefits: clearer and syntax is more readable 

# def day_of_week(day):
#     match day:
#         case 1: 
#             return "It sunday"
#         case 2:
#             return "It monday"
#         case 3:
#             return "It tuesday"
#         case 4:
#             return "It wednesday"
#         case 5:
#             return "It thursday"
#         case 6:
#             return "It friday"
#         case 7:
#             return "It saturday"
#         case _:
#             return "Invalid day"
        
        
# print(day_of_week(7))

# def is_weekend(day):
#     match day:
#         case "Sunday" | "Saturday": 
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return "Invalid day"

# print(is_weekend("Monday"))


# module = a file containing python code that can be imported into other python files
# import module_name
# useful to break up large program resuable separate files

# print(help("modules"))


# import math
# import math as m
# from math import pi

# print(pi)

# Variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) local -> enclosing -> global -> built-in


# def func1():
#     a= 1
#     print(a)
    
# def func2():
#     a = 2
#     print(a)
    
    
# func1()
# func2()


# from math import e


# def fun1():
#     print(e)
    
# e = 2.374343
    
# fun1()


# if__name__ == "__main__": (this script can be imported or run standlone)
#  functins and classed in the module can be reused
# without the main block of  code executing 

# def main():
#     pass

# if __name__ == ' __main__':
#     main()
