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
    expression = f"{get_random_num()} {action} {get_random_num()}"
    print(f"Question: {expression}")
    return expression


def get_correct_answer(expression):
    list_expression = expression.split()
    left_operand, action, right_operand = [*list_expression]
    left_operand, right_operand = int(left_operand), int(right_operand)
    match action:
        case "+":
            return left_operand + right_operand
        case "-":
            return left_operand - right_operand
        case "*":
            return left_operand * right_operand 
        case _:
            return None