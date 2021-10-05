from question_model import Question

question_data = [
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The common software-programming acronym ; comes from the term Interlocalization.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The first computer bug was formed by faulty wires.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The very first recorded computer bug was a moth found inside a Harvard Mark II computer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "Windows NT is a monolithic kernel.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "MacOS is based on Linux.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Time on Computers is measured via the EPOX System.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "Android versions are named in alphabetical order.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]

question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    question_bank.append(Question(question_text, question_answer))
