import random

import prompt


def welcome_user():
    ''' Ask the user's name, greet him and return user_name'''
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!") 
    return user_name


def gen_random_num():
    ''' Generate random number and return him'''
    display_number = random.randint(1, 50)
    return display_number


def gen_expression():
    ACTIONS = ("+", "-", "*")
    action = random.choice(ACTIONS)
    return f"{str(gen_random_num())} {action} {str(gen_random_num())}"    


def get_answer_user():
    ''' Get answer user from input string and return him'''
    user_answer = prompt.string('Your answer: ')
    return user_answer

def main():
    # Get user_name from func welcome_user
    user_name = welcome_user()
    print('What is the result of the expression?')
    expression = gen_expression()
    print(f"Question: {expression}")

if __name__ == "__main__":
    main()  