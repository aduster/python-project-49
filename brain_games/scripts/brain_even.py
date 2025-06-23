import random

import prompt


def welcome_user():
    ''' Ask the user's name, greet him and return name'''
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    return user_name


def gen_random_num():
    ''' Generate random number and return him'''
    display_number = random.randint(1, 50)
    return display_number


def get_answer_user():
    ''' Get answer user from input string and return him'''
    user_answer = prompt.string('Your answer: ')
    return user_answer


def even_number(number):
    ''' Get answer computer and return him'''
    if number % 2 == 0:
        return "yes"
    else:
        return "no"    


def main():
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
        print(f"Congratulations, {user_name}!")
            

if __name__ == "__main__":
    main()        