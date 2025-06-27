import random


def game_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    ''' Create question and return him'''
    one_number = str(random.randint(1, 100))
    print(f"Question: {one_number}")
    return one_number


def get_correct_answer(number):
    if int(number) % 2 == 0:
        return "yes"
    else:
        return "no"