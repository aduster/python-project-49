from brain_games import cli


def main():
    # Get user_name from func welcome_user
    user_name = cli.welcome_user()
    print(f"Hello, {user_name}!") 


if __name__ == "__main__":
    main()