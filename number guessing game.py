import random
import math

#user select his range
#selected range needs to belong to Integer
#random integer will be selected by the system 
#user has to guess this integer in minimum number of guesses 
#minimum number of guesses depend upon range, we have formula to calculate it

#user inputs the lower bound and upper bound of the range
lower_bound = int(input("This will be lower bound: "))
upper_bound = int(input("This will be upper bound: "))

#generate random integrer in the range
guessing_number = random.randint(lower_bound, upper_bound)
print(f"You have only {guessing_number} chances to guess!")

#user is guessing their number
user_number = int(input("Guess your number: "))

while guessing_number > user_number:
    how_many_guesses = 0
    print("Try again! You guessed too hight!")
else:
    print("Try againg! You huessed too small!")

#calculating how many times user can guess
guesses = int(math.log(upper_bound - lower_bound +1))

if how_many_guesses == guesses:
    print("Congratulations!")
else:
    print("Better Luck next time!")
