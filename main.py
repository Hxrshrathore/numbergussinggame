import random

def get_user_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!\n")
    min_number = get_user_input("Please enter the minimum number: ", 1, 10000)
    max_number = get_user_input("Please enter the maximum number: ", min_number + 1, 10000)

    target_number = random.randint(min_number, max_number)
    attempts = 0

    while True:
        attempts += 1
        user_guess = get_user_input(f"Attempt {attempts}: ", min_number, max_number)

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.\n")
            break
        elif user_guess < target_number:
            print("The number is higher.")
        else:
            print("The number is lower.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print("Thank you for playing the Number Guessing Game!")

if __name__ == "__main__":
    number_guessing_game()
