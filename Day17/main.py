from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    new_ques = Question(question["question"], question["correct_answer"])
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while (quiz.still_has_question()):
    quiz.next_ques()

print("You have completed the quiz")
print(f'Your final score was {quiz.score}/{quiz.question_number}')
