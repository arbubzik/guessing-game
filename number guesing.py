import random
import math
#creating lower and upper bound
lower_bound = int(input("Choose your lower bound of the range: "))
upper_bound = int(input("Choose your upper bound of the range: "))
#calculating how many times user can guess
x = upper_bound - lower_bound
guessing_times_not_rounded = math.log(x, 2)
guessing_times_rounded = round(guessing_times_not_rounded)
print("You only have " + str(guessing_times_rounded) + " chances to guess the integrer!")
#getting random number in the range that user did input
random_number_generated = random.randint(lower_bound, upper_bound)

#starting number of guesses
count = 0
while count < guessing_times_rounded:
    count +=1

    #taking input from user
    guessing_number = int(input("Guess the number: "))

    if random_number_generated == guessing_number:
        print("Congratulations you did it in", count, " try")
        #is user guessed, loop breaks
        break
    elif random_number_generated > guessing_number:
        print("You guessed too small!")
    elif random_number_generated < guessing_number:
        print("You guessed to high!")

#if user is guessing too much
if count >= random_number_generated:
    print("The number is", random_number_generated)
    print("Better luck next time!")