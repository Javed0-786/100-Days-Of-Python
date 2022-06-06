'''student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
'''
import pandas


name = input("Enter Your Name: ")
data = pandas.read_csv("data.csv")
letters = [letter.upper() for letter in name]
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# my_dict = {letter: nato for (letter, nato)
#            in nato_dict.items() if letter in letters}


def generate_phonetic():
    global nato_dict, letters, data
    name = input("Enter Your Name: ")
    data = pandas.read_csv("data.csv")
    letters = [letter.upper() for letter in name]
    nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


Run = True
while Run:
    try:
        my_list = [nato_dict[letter] for letter in letters]
        Run = False
    except KeyError:
        print("Please Enter a valid Name")
        generate_phonetic()

    else:
        print(my_list)


# for letter in letters:
#     for (index, row) in data.iterrows():
#         if letter == row.letter:
#             print(letter, ':', row.code)
