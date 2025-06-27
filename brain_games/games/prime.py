import random


def game_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    ''' Create question and return him'''
    one_number = str(random.randint(1, 100))
    print(f"Question: {one_number}")
    return one_number


def get_correct_answer(number):
    flag = True
    number = int(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            flag = False
            break
    if number > 1 and flag:
        return "yes"
    else:
        return "no"