# %%

# MILESTONE 2 #

# List of Fruits

word_list = ["apple","lychee", "mangosteen", "clementine","grape"]

# %%
print(word_list)

# %%

# BMI checker

def BMI_check(height, weight):

    bmi= (weight/height**2)
    if bmi <18.5:
        print("Your BMI is {}. You're In the underweight range.".format(bmi))
    elif bmi >= 18.5 and bmi <= 24.9: 
        print("Your BMI is {}. You're In the healthy weight range.".format(bmi))
    elif bmi >=25 and bmi <= 29.9: 
        print("Your BMI is {}. You're In the overweight range.".format(bmi))
    elif bmi >= 30 and bmi <= 39.9: 
        print("Your BMI is {}. You're In the obese range.".format(bmi))

# %%

#Testing variations

BMI_check(1.83, 85)
BMI_check(1.55, 61)
BMI_check(2.09, 135)

# %%

# Flight Safety Checker

def check_safety(altitude,airspeed):
    if altitude < 100 or altitude > 50000:
        print("This atlitude is unsafe")
    elif airspeed < 60 or airspeed > 500: 
        print("This atlitude is unsafe")
    else: 
        print("This atlitude is safe!")

# %%

#Testing variations

check_safety(25000, 300)
check_safety(50001, 250)
check_safety(90, 125)

# %%

# Order of conditions
# Original order was:

##  x = int(input('Enter a number: '))
##  if x > 0: 
##      print('x is greater than 0')
##  elif x > 15:
##      print('x is greater than 15')
##  elif x > 20:
##      print('x is greater than 20')
##  else:
##      print('x is less than 0')

# the above will print the first conditional that is met, therefore, if x = 16, it would print only x is greater than 15.

#Corrected version below.
x = int(input('Enter a number: '))

if x > 20: 
    print('x is greater than 20')
elif x > 15:
    print('x is greater than 15')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is less than 0')

# %%

# Unique Elements in the List

my_list = ["a","f","e","d","c","b","z","h"]
x = len(my_list)
i = 0
a = 0

while i < x:
    
    for ii in range(i+1,x):
        
        if my_list[i] == my_list[ii]:
            a+=1
    i+=1

if a > 0:
    print("There are duplicates in this list")
else: 
    print("No duplicates")       
        
#I know this is somewhat very inefficient but it works.

# %%

# Rock, Paper, Scissors

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
if list_1 == list_2:
    print('The lists are the same.')
else:
    print('The lists are different.')

# %% 

# Chose to do the rock paper scissors this way. Inefficient but it works.

def rps(player1, player2):
    if player1 == "rock":
        if player2 == "rock":
            print ("It's a tie!")
        elif player2 == "scissors":
            print("Player 1 wins!")
        elif player2 == "paper":
            print("Player 2 wins!")
        else:
            print("Invalid input")
    elif player1 == "scissors":
        if player2 == "rock":
            print ("Player 2 wins!")
        elif player2 == "scissors":
            print("It's a tie!")
        elif player2 == "paper":
            print("Player 1 wins")
        else:
            print("Invalid input")
    elif player1 == "paper":
        if player2 == "rock":
            print ("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")
        elif player2 == "paper":
            print("It's a tie!")
        else:
            print("Invalid input")
    else:
        print("invalid input")

rps("scissors", "scissors")

# %%

#Example lines to import class/functions from modules.

from pickle import FALSE
import pandas as pd
from pandas import DataFrame

# %%

#AiCore Task 2 - Choose a random word from the list.

#Step 1 +2 

import random

#Step 3 

x = random.choice(word_list)

print(x)

# %%

#Task 3 - Ask the user for an input

guess = input("Enter a single letter!")
print(guess)

# %%

#Task 4 - Check that the input is a single character

guess = input("Enter a single letter!")

if len(guess) ==1 and type(guess) == str:
    print("Good guess!")
else:
    print("That is not a a valid input")
    
# %%

#Task 5 - Start documenting your experience....

#Uploaded milestones and descriptions onto GitHub.

#--------------------------------------------------

# %% 

# MILESTONE 3 #

# Task 1: Iteratively check if the input is a valid guess

x = True
while x == True:
    guess = input("Guess a letter in the word.")
    if len(guess) == 1:
        x = False
        print(guess)
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        
# %%

# Task 2: Check whether the guess is in the word
import random

word_selection = ["Shenanigans","Bamboozle", "Bodacious", "Brouhaha", "Canoodle", "Gnarly", "Goggle", "Gubbins", "Malarkey", "Nincompoop" ]

word_of_the_run = random.choice(word_selection).lower()

# print(word_of_the_run)

# Guess a letter in the randomly selected word.

x= True
while x== True:
    guess = input("Guess a letter in the word. Use lowercase only..thank you")
    if len(guess) == 1 and guess in word_of_the_run:
        x = False
        print("Good guess '{}' is in the word.".format(guess))
    elif len(guess) != 1:
        print("Invalid letter. Please, enter a single alphabetical character.")
    else:
        print("Sorry, '{}' is not in the word. Try again".format(guess))
       

# %%

#Pre-requisite tasks

# Void Functions

def void_function():
    print("This is a void function")

void_result = void_function()

# The above line by itself, prints the message because it calls the function - and thus prints the message.

print(void_result)

# However, message printed is not assigned to a variable during the calling of the void_function function. Thus nothing is stored in void_result variable.

# %%

#Range Checker

def in_range(lower_bound, upper_bound, number):
    
    if int(number) >= int(lower_bound) and int(number) <= int(upper_bound):
        print( "{number} is between  {lower_bound} and {upper_bound}")
    elif int(number) < int(lower_bound) or int(number) > int(upper_bound):
        print( "{number} is NOT between  {lower_bound} and {upper_bound}") 
    else: 
        print("Likely an invalid input format. Please make sure arguments are numbers")
# Tests..

in_range(1,5,2)
in_range(3,5,2)
in_range(5,100,98)

# %%

# Volume of a Sphere   (V=4/3 π r^3)  radius in metres

def volume_of_sphere(radius):
    pi=3.14
    radius_cube = int(radius)**3
    volume = 4/3 * pi * radius_cube
    return volume

sphere = volume_of_sphere(8)
print(sphere)

#function could be one line - but it is less modifiable (e.g. if input units are not limited to metres)

def volume_of_sphere_short(radius):
    return 4/3 * 3.14 * radius**3

sphere2 = volume_of_sphere_short(8)
print(sphere2)

# %%

#Challenge for a function!

#Make a function that calculates how many portions of cheesecake (or any other food you like) you can make from the ingredient amounts you have.
# E.g. making a oreo cheesecake

def can_we_feed_5000(oreos_n,butter_g,cream_cheese_g,sugar_g,vanilla_extract_tsp,whipping_cream_cups):
    #ingredient list and numbers
    oreo=39
    butter=60
    cream_cheese= 453
    sugar = 1
    vanilla_extract= 1
    whipping_cream= 400
    
    o=  (oreos_n / oreo)
    b=  (butter_g / butter)
    cc= (cream_cheese_g / cream_cheese)
    s=  (sugar_g/ sugar)
    ve= (vanilla_extract_tsp / vanilla_extract)
    wc= (whipping_cream_cups/ whipping_cream)

    ratio = [o,b,cc,s,ve,wc]
    ratio.sort()
 
    print("You have enough of each ingredient to make {} oreo cheesecakes.".format(int(ratio[0])))
    
can_we_feed_5000(78,120,1000,10,20,5000)

#will 10000 of everything enough to make for 5000 portions? 

can_we_feed_5000(10000,10000,10000,10000,10000,10000)

#nope cream cheese and whipping cream needs a lot more...

can_we_feed_5000(1000000,1000000,1000000000,10000000,10000000,2000000)

# %%

# Default Arguments

printlist = {"test":1,"haha":2, "huhu":4}
list = ["test"]

def check_dict(list):
    attributes_to_print = printlist
    x=0
    while x < len(list):
        if list[x] in printlist.keys():
            print(list[x],"exists in the word")
            x +=1
        else:
            print("{list[x]} does not exist")
    
check_dict(list)
# %%

# Profile Validation

import re

# Regular Expressions

def name_check(name):
    if re.search("!@£$%^&*()",name) == None:
        return name
    else: 
        return "invalid format -please try again"
    
def age_check(age):
    if int(age) > 12:
        return age
    else: 
        print("You must be over 12.")

def email_check(email):
    if re.search( """\\w@\\w""",email) != None:
        return email
    else: 
        return "invalid format -please try again"

def profile_check(name,age,email):
    profile = []
    profile.append(name_check(name))
    profile.append(age_check(age))
    profile.append(email_check(email))
    print(profile)
    
profile_check("DC",28,"dc.choi@kcl.ac.uk")

# %%

#Factorial Function

def factorial(number):
    if number ==0:
        return 1
    else:
        return number * factorial((number-1))

print(factorial(4))
# %%

# Recursive Fibonacci Function

# 0 1 1 2 3 5 8 13 21 ....

def fibonacci_seq(number):
    if number == 0:
        return 0
    elif number ==1:
        return 1
    else:
        return (fibonacci_seq(number-1) + fibonacci_seq(number-2))

x=35
list=[]
while x>=1:
    list.append(str(fibonacci_seq(x-1)))
    x -=1
    print(fibonacci_seq(x))
list.sort()
print(list)

# %%

# Inverse a string

word_list = ["hello", "hi"]
list= []
for words in word_list:
    for letter in words:
        
        list.append(letter)
list.reverse()
print(list)

# %%

#Palindrome Checker

palindromes = ['racecar','bob','neveroddoreven','poop']
non_palindromes = ['racecars', 'boba', 'evenstevens','diarrhea']

def check_if_palindrome(list):
    list =[]
    for word in list:
        x = len(word)
        if x % 2 == 0:
            for letter in word:
                list.append(letter)
                print(list)
                two = list.reverse()
                print(two)

# %%
list= []
word = "racecars"
for letter in word:
    list.append(letter)
    x= list
    y= list

# %%

#Task 3 - Create functions to run the checks   

def check_guess(guess,word):
    x = True
    word = word.lower()
    while x==True:
        if  guess in word:
            x = False
            print("Good guess '{}' is in the word.".format(guess))
        else:
            print("Sorry, '{}' is not in the word. Try again".format(guess))
            guess = input("Guess a letter in the word.")
            
def ask_for_input(word):
    x= True
    while x == True:
        guess = input("Guess a letter in the word. Use lowercase only..thank you")
        if guess == guess.capitalize():
            guess = input("Invalid letter. Please, enter a lowercase character.")
        elif len(guess) == 1:
            x = False
        elif len(guess) != 1:
            guess = input("Invalid letter. Please, enter a single alphabetical character.")
        else:
            break
    check_guess(guess,word)

# %% 

#Testing the ask_for_input function using a few example words.

word_1 = 'Hello'
word_2 = 'Tatratea'
word_3 = 'Hangman'
word_4 = 'AirPods'

ask_for_input(word_1)
ask_for_input(word_2)
ask_for_input(word_3)
ask_for_input(word_4)

# %%

# Task 4: Update your documentation

# Milestone 3 scripts cleaned and uploaded into GitHub repo (https://github.com/chedongchan/AiCore_Milestones/)
# Script file and Documentation updated, added, committed and pushed into github repo using the terminal.
