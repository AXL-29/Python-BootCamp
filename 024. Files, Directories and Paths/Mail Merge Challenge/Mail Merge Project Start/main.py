"""
Automates the creation of personalized invitation letters.

Reads a template letter, replaces the [name] placeholder with each
invited name, and saves individual letters to the output folder.
"""

# Read the letter template once
with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    template = letter_file.read()

# Process each invited name
with open("./Input/Names/invited_names.txt", "r") as names_file:
    for name in names_file:
        clean_name = name.strip()
        personalized_letter = template.replace("[name]", clean_name)

        # Write the personalized letter
        output_path = f"./Output/ReadyToSend/letter_for_{clean_name}.txt"
        with open(output_path, "w") as output_file:
            output_file.write(personalized_letter)
