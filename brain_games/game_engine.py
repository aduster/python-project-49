import prompt


def welcome_user():
    ''' Ask the user's name, greet him and return user_name'''
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!") 
    return user_name


def start_game(name_game):
    # User greeting and save your name
    user_name = welcome_user()
    # Tell the rules of the game
    print(name_game.game_rules())
    # The game start now, and stop after thee correct answer or one wrong answer
    correct_answer_count = 0
    while correct_answer_count < 3:
        question = name_game.get_question()
        user_answer = name_game.get_user_answer()
        correct_answer = name_game.get_correct_answer(question)
        if name_game.get_comparison(user_answer, correct_answer):
            print("Correct!")
            correct_answer_count += 1
            continue
        else:
            break
    if correct_answer_count == 3:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"'{user_answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")



    


    
