student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    if student_scores[name] >= 90:
        student_grades[name] = "A+"
    elif student_scores[name] >= 80:
        student_grades[name] = "A"
    elif student_scores[name] >= 70:
        student_grades[name] = "B+"
    elif student_scores[name] >= 60:
        student_grades[name] = "B"
    elif student_scores[name] >= 50:
        student_grades[name] = "C+"
    elif student_scores[name] >= 40:
        student_grades[name] = "C"
    else:
        student_grades[name] = "F"


# 🚨 Don't change the code below 👇
print(student_grades)
