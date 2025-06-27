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
    

""" def main():
    # Get user_name from func welcome_user
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # The game begin now, and finish win after 3 correct answer
    correct_answer_count = 0
    while correct_answer_count < 3:
        display_number = gen_random_num()
        print(f"Question: {display_number}")
        user_answer = get_answer_user()
        correct_answer = even_number(display_number)
        if not (user_answer == "yes" or user_answer == "no"):
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        elif correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        elif correct_answer == user_answer:
            print("Correct!")
            correct_answer_count += 1
            continue
    else:
        print(f"Congratulations, {user_name}!") """
