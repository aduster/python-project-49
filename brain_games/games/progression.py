import random


def game_rules():
    return "What number is missing in the progression?"


def get_random_number(start, stop):
    ''' Generate random number and return him'''
    number = random.randint(start, stop)
    return number


def get_question():
    start = get_random_number(1, 25)
    step = get_random_number(1, 15)
    missing_index = get_random_number(1, 9)
    progression = []
    for index in range(10):
        current = start + index * step
        progression.append(current)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."  
    print("Question:", end=" ")
    print(*progression)
    return correct_answer


def get_correct_answer(question):
    return question    