from random import randrange as randr

'''
Ask a user to guess a number
generate a rondom number and check if it matches the user's input
tell user if their guess is correct, too high or too low until they get it right
enter 0 to exit

create a program that guesses the user's input number
Enter -1 to exit
'''

user_num = -1
comp_guess = randr(11)

try:
    user_num = int(input("Guess a number between 0 & 10\nEnter -1 to exit\t:"))
    print(f"\nYou guessed {user_num}")
except ValueError as e:
    print(f"\nERROR: Input must be a number/int\n{str(e).upper()}")

while user_num != -1:
    if comp_guess == user_num:
        print("You guessed right!")
        break
    else:
        if comp_guess > user_num:
            print("\nYour guess is low")
        else:
            print("\nYour guess is high")
        print("Oops! Wrong guess, try again")
        user_num = int(input("Guess a number between 0 & 10\nEnter -1 to exit\t:"))
        print(f"\nYou guessed {user_num}")