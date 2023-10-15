import random
import os


def choose_word(category, difficulty):  # Lists of words for dif categories
    words = {
        "foods": {
            "easy": [
                "burger", "banana", "sushi", "pizza", "orange",
                "shrimp", "steak", "cake"
            ],
            "medium": [
                "papaya", "lasagna", "raspberry", "pudding",
                "kebab", "paprika", "soup"
            ],
            "hard": [
                "prune", "strawberry", "wasabi", "nachos",
                "borscht", "quinoa", "gnocchi"
            ]
        },
        "cars": {
            "easy": [
                "bmw", "audi", "ford", "mini", "lexus", "subaru",
                "mazda", "renault", "fiat", "hyundai", "kia"
            ],
            "medium": [
                "toyota", "chevrolet", "honda", "dacia",
                "porsche", "opel", "pagani", "bentley", "volkswagen"
            ],
            "hard": [
                "mercedes", "ferrari", "lamborghini", "delorean",
                "koenigsegg", "detomaso", "holden", "rimac"
            ]
        },
        "countries": {
            "easy": [
                "usa", "austria", "turkey", "hungary", "sweden",
                "russia", "italy", "mexico", "belgium"
            ],
            "medium": [
                "afghanistan", "kazachstan", "turkmenistan",
                "thailand", "panama", "switzerland", "netherlands"
            ],
            "hard": [
                "liechtenstein", "kenya", "madagascar", "myanmar",
                "bangladesh", "nepal", "djibouti", "kyrgyzstan"
            ]
        }
    }

    return random.choice(words[category][difficulty])


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """

    ]
    return stages[tries]


def print_logo_and_explanation():  # Welcome message for the game
    # and information about the game
    logo = """
    ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
    ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
    ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
    ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
    ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    """
    print(logo)
    explanation = (
        "\nWelcome to Hangman!\n\n"
        "How to Play:\n"
        "1. Choose a category and difficulty level.\n"
        "2. Try to guess the word - one letter at a time.\n"
        "3. You can make up to 6 wrong guesses.\n"
        "4. If you guess the word before running out of tries, you win!\n"
        "5. Have fun!\n"
    )
    print(explanation + "\n")


def play_again():  # Prompts user to play again, validates input.
    while True:
        play_again_input = input(
            "\nWould you like to play again? (y/n) ").strip().lower()
        if play_again_input in ['y', 'n']:
            return play_again_input == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def play_hangman():
    print_logo_and_explanation()

    # Prompt user to start the game
    start_game = input("Press 'y' to start the game: " + "\n").strip().lower()

    # Validate user input for starting the game
    while start_game != 'y':
        print("Error, please press 'y' to start game")  # Error message
        start_game = input("Press 'y' to start the game: ").strip().lower()

    # Initialize category variable
    category = ""
    while category not in ["foods", "cars", "countries"]:
        category = input(
            "Which category of words would you like to guess "
            "(foods/cars/countries)? " + "\n"
        ).strip().lower()

        if category not in ["foods", "cars", "countries"]:
            print("Error Message: Please choose foods, cars, or countries.")

    # Initialize difficulty variable
    difficulty = ""
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input(
            "Choose word difficulty (easy, medium, hard): " + "\n"
        ).strip().lower()

        if difficulty not in ["easy", "medium", "hard"]:
            print("Error Message: Please choose easy, medium, or hard.")

    word = choose_word(category, difficulty)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print("\n" + "Let's play Hangman!")
    print("\n" + display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:  # Main game loop
        guess = input("\nPlease guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():  # Validate input
            if guess in guessed_letters:
                print("You already guessed", guess)  # Repeat guess message
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)  # Track guessed letter
                print("Guessed Letters:", guessed_letters)
                print("Remaining tries:", tries)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)  # Convert to list
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess  # Update guessed letters
                # Convert back to string
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) > 1:
            print("Error: Only one letter a a time allowed")

        else:
            print("Error: Only letters allowed")
            continue  # Skip the rest of the loop if the input is invalid

        print("\n" + display_hangman(tries) + "\n")
        print(word_completion + "\n")
        print("\n")

    if guessed:
        print("\nCongrats, you guessed the word! You win ( ͡ᵔ ͜ʖ ͡ᵔ)")
    else:
        print("\nSorry, you ran out of tries. The word was " +
              word + ". Maybe next time! ( ͡ᵔ ︵ ͡ᵔ)")

    return play_again()


if __name__ == "__main__":
    while play_hangman():  # Executes hangman game in a continuous loop.
        pass  # If user chooses no, print message
    print("\nThank you for playing, have a nice day! ┏( ͡ᵔ _⦣ ͡ᵔ)┛ ")
