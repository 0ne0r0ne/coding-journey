import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)

user_world = input("Enter a world").upper()

user_results = [new_dict[i] for i in user_world]

print(user_results)

