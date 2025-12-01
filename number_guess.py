import random
print('Welcome to the Number Guessing game!')
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard'.: ")
guess = int(input("Make a guess: "))
selected_number = random.randint(1,100)
won = False

if difficulty_level == 'easy':
    remaining_attempts = 10
else:
    remaining_attempts = 5

for i in range(remaining_attempts):
    remaining_attempts_current = remaining_attempts - i -1
    if selected_number == guess:
        print(f"You got it! The answer was {guess}")
        won = True
        break
    elif selected_number > guess:
        print("Your guess is too low. Try again.")
        print(f"You have {remaining_attempts_current} attempt remaining. ")

        guess = int(input("Make a guess: "))
    else:
        print("Your guess is too high. Try again.")
        print(f"You have {remaining_attempts_current} attempt remaining. ")
        guess = int(input("Make a guess: "))

if not won:
    print("You've run out of guesses. Refresh the page to run again")




