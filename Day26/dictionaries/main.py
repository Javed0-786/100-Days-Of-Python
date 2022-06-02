# import random

# students = ["Ravi", "Ramesh", "Rohit", "Raj", "Mohit", "Mukund"]

# result = {student: random.randint(1, 100) for student in students}
# result = {'Ravi': 6, 'Ramesh': 5, 'Rohit': 80,
#           'Raj': 22, 'Mohit': 80, 'Mukund': 60}

# passed_students = {student:  result[student]
#                    for student in result if result[student] > 40}

# print(passed_students)


# Exercise 1
'''
sentence = "What is the Airspeeed Velocity of an Unladen Swallow?"

words = sentence.split(" ")

result = {word: len(word) for word in words}

print(result)

# {'What': 4, 'is': 2, 'the': 3, 'Airspeeed': 9, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
'''


# Exercise 2
'''
weatehr_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Satuday": 22,
    "Sunday": 24,
}

weatehr_f = {day: (temp * 9/5) + 32 for (day, temp) in weatehr_c.items()}
print(weatehr_f)
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Satuday': 71.6, 'Sunday': 75.2}
'''
