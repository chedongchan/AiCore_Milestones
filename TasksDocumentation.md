# AiCore Hangman Project Documentation

> Hangman Game Project. 

## Milestone 1: Set up the environment

- Q: What have you built? 
- A: Set up Github Repository. New directories.

- Q: What technologies have you used? 
- A: VS Code, MiniConda and Git. Command line - using terminal commands to manipulate files and directories. 

- Q: Why have you used those?
- A: VS Code works as the text editor. MiniConda is a useful virtual environment generating software. Git is a version control system that allows  everyone to track changes, revert back to a previous (usually 'working' version), contribute towards a final product (main/master branch).


## Milestone 2: Create the variables for the game

- Q: What have you developed within the environment?
- A: Writing scripts that can create, manipulate numbers, strings, lists, overall assinging/storing them to variables which can be called and/or printed.

- Q: What utilities have you learnt this time?
- A: I learnt to install pacakges in base and virtual environments for use. Importing modules that have useful functions embedded inside them.


```python
"""
# %%

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
        


for i in range(x):
    if my_list[i] in (my_list-list(my_list[i])):
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

"""

```
