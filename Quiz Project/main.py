from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score} out of {quiz.question_number}.")
