import random


def game_rules():
    return "What is the result of the expression?"


def get_random_num():
    ''' Generate random number and return him'''
    display_number = random.randint(1, 100)
    return display_number


def get_question():
    ''' Create question and return him'''
    ACTIONS = ("+", "-", "*")
    action = random.choice(ACTIONS)
    expression = f"{str(get_random_num())} {action} {str(get_random_num())}"
    print(f"Question: {expression}")
    return expression


def get_correct_answer(expression):
    list_expression = expression.split()
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