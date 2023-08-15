from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_item in question_data:
    question = Question(question_item["text"], question_item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.stil_has_questions():
    quiz.nextQuestion()

print("You've completed the quiz!")
print(f"your final score is {quiz.score}/{quiz.question_number}")