"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 

Extras:
    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
    (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""

name = input("Please enter your name: ")
age = input("Please enter your age: ")
random_number = int(input("Please input random number: "))

current_year = 2022
future_year = (100 - int(age)) + 2022

statement = "\n{} you will be 100 in the year {}".format(name, future_year)

print(str(statement) * random_number)