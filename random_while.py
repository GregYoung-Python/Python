from random import choice
questions = ["Why is the sky blue?", "Why do birds sing?",
             "What day is it?", "What time is it?", "What is your name?"
                     ]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just because":
    answer = input("why?").strip().lower()
