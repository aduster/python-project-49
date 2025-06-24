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


def get_user_answer():
    ''' Get answer user from input string and return him'''
    user_answer = prompt.integer('Your answer: ')
    return user_answer


def get_correct_answer(string_expression):
    list_expression = string_expression.split()
    left_operand, action, right_operand = [*list_expression]
    match action:
        case "+":
            return int(left_operand) + int(right_operand)
        case "-":
            return int(left_operand) - int(right_operand)
        case "*":
            return int(left_operand) * int(right_operand) 
        case _:
            return None


def main():
    # Get user_name from func welcome_user
    user_name = welcome_user()
    print('What is the result of the expression?')
    # The game begin now, and finish win after 3 correct answer
    correct_answer_count = 0
    while correct_answer_count < 3:
        string_expression = gen_expression()
        print(f"Question: {string_expression}")
        user_answer = int(get_user_answer())
        correct_answer = get_correct_answer(string_expression)        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")       


if __name__ == "__main__":
    main()  