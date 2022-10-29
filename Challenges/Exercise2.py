"""
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

number = int(input("Please input a number: "))
check = int(input("Please enter a second number to check if it is divisble by {}: ".format(number)))

def odd_even(number):
    odd_even = (int(number) % 2)
    if odd_even == 0:
        print("number is even")
    elif odd_even == 1:
        print("number is odd")
    else:
        print("you got me")

#x = int(input("Please Enter Number"))

def multiple_of_four(number):
    if number%4 == 0:
        print("number is divisible by 4")
    else:
        print("number is not divisible by 4")

def divisible(number, check):
    if number%check == 0:
        print("{} is divisble by {}".format(number, check))
    else:
        print("{} is not divisble by {}".format(number, check))


#odd_even(number)
#multiple_of_four(number)

divisible(number, check)