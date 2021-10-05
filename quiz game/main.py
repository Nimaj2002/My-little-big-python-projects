from quiz_brain import QuizBrain
from data import question_bank

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("\nYou Completed the Quiz")
print(f"Your score was {quiz.score}/{quiz.question_number}")