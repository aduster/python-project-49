import random

import prompt


def game_rules():
    return "Find the greatest common divisor of given numbers."


def get_random_num():
    ''' Generate random number and return him'''
    display_number = random.randint(1, 100)
    return display_number


def get_question():
    string_two_numbers = f"{str(get_random_num())} {str(get_random_num())}"
    print(f"Question: {string_two_numbers}")
    return string_two_numbers


def get_user_answer():
    ''' Get answer user from input string and return him'''
    user_answer = prompt.integer('Your answer: ')
    return user_answer


def get_correct_answer(question):
    string_numbers = question.split()
    int_numbers = [int(item) for item in string_numbers]
    left_number, right_number = [*int_numbers]
    while left_number != 0 and right_number != 0:
        if left_number > right_number:
            left_number = left_number % right_number
        else:
            right_number = right_number % left_number 
    return left_number + right_number