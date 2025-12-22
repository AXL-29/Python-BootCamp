import pandas


#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()
phonetic_code = [nato_dict[letter] for letter in user_input if letter in nato_dict]
print(phonetic_code)

