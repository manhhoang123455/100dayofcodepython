from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    q = Question(question_text, question_answer)
    question_bank.append(q)

qz = QuizBrain(question_bank)
while qz.still_has_question():
    qz.next_question()