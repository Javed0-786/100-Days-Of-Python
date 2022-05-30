# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt")as starting_letter:
    content = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()


for i in range(1, 9):
    name = names[i-1].strip("\n")
    changed = content.replace("[name]", name)

    with open(f"./Output/ReadyToSend/file{i}.txt", "w") as letter:
        letter.write(changed)
