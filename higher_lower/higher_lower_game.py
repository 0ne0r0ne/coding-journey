import random
import data_0

game = True
current_score = 0

A = {}
B = {}

def choice():
    """This function chooses dictionary elements for A and B"""
    global A
    global B
    A = random.choice(data_0.data)
    B = random.choice(data_0.data)
    while A == B: #important
        A = random.choice(data_0.data)
        B = random.choice(data_0.data)
choice()

#main_loop
while game:
    chosen_letter = input(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.\n"
                          f"Against B: {B['name']}. {B['description']}, from {B['country']}.\n"
                           "Who has more followers? Type 'A' or 'B' ")
    def compare():
        """This function compares A and B and gives us the biggest followers"""
        if A['follower_count'] > B['follower_count']:
            return "A"
        else:
            return "B"

    if chosen_letter == "A":
        if compare() == "A":
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
            if B in data_0.data:
                data_0.data.remove(B)
            if A in data_0.data:
                data_0.data.remove(A)
            B = random.choice(data_0.data)
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}.")
            game = False
    else:
        if compare() == "B":
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
            if B in data_0.data:
                data_0.data.remove(B)
            if A in data_0.data:
                data_0.data.remove(A)
            A = B
            B = random.choice(data_0.data)
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game = False










