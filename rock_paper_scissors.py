import random
options = ["Rock", "Paper", "Scissors"]
user_options = input("Rock, Paper or Scissors\n")
computer_options = random.choice(options)

if user_options == computer_options:
    print("It's a tie!")
elif user_options == "Rock" and computer_options == "Paper":
    print("You lost!")
elif user_options == "Rock" and computer_options == "Scissors":
    print("You won!")
elif user_options == "Paper" and computer_options == "Rock":
    print("You won!")
elif user_options == "Paper" and computer_options == "Scissors":
    print("You lost!")
elif user_options == "Scissors" and computer_options == "Rock":
    print("You lost!")
elif user_options == "Scissors" and computer_options == "Paper":
    print("You won!")

print(f"Your choice is {user_options} and computer choice is {computer_options}")






