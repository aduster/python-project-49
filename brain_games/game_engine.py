import prompt


def welcome_user():
    ''' Ask the user's name, greet him and return user_name'''
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!") 
    return user_name


def get_user_answer():
    ''' Get answer user from input string and return him'''
    return prompt.string('Your answer: ')


def is_win(user_answer, correct_answer):
    if correct_answer in ("yes", "no"):
        return user_answer == correct_answer
    else:
        return int(user_answer) == correct_answer 


def get_result_game(user_name, correct_answer, user_answer, win_count):
    # Win after thee correct answer in a row
    if win_count == 3:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"'{user_answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")


def game_process(name_game):
    # User greeting and save name
    user_name = welcome_user()
    # Tell the rules of the game
    print(name_game.game_rules())
    # The game start now, and stop after thee correct answer or one wrong answer
    win_count = 0
    while win_count < 3:
        question = name_game.get_question()
        user_answer = get_user_answer()
        correct_answer = name_game.get_correct_answer(question)
        if not is_win(user_answer, correct_answer):
            break
        else:
            win_count += 1
            print("Correct!")
    # Now let's sum up the game
    get_result_game(user_name, correct_answer, user_answer, win_count)        
    

    


    
