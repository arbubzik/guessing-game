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

#starting number of guesses
guesses = 0

#calculating how many times user can guess
guesses_attempts = round(math.log(upper_bound - lower_bound + 1, 2))
print(f"You have only {guesses_attempts} chances to guess!")

#user is guessing their number
#user_number = int(input("Guess your number: "))

while guesses < guesses_attempts:
    guesses +=1

    #user is guessing their number
    user_number = int(input("Guess your number: "))

    if user_number == guessing_number:
        print(f"Congratulations! you did it in {guesses} try")

        break
    elif guessing_number < user_number:
        print("Try again! You guessed too hight!")
    elif guessing_number > user_number:
        print("Try againg! You guessed too small!")

#if numbers of attempts are too high, we have to check it and print this message in the end
if guesses >= guesses_attempts:
    print("Better luck next time!")
    print(f"The number is {guessing_number}")
