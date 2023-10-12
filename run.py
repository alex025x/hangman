import random
import os

def choose_word(category, difficulty):
    words = {
        "foods": {
            "easy": ["burger", "banana", "sushi", "pizza", "orange"],
            "medium": ["papaya", "lasagna", "raspberry", "pudding", "kebab"],
            "hard": ["prune", "strawberry", "wasabi", "nachos", "borscht"]
        },
        "cars": {
            "easy": ["bmw", "audi", "ford", "mini", "lexus", "subaru"],
            "medium": ["toyota", "chevrolet", "honda", "dacia", "porsche", "opel"],
            "hard": ["mercedes", "ferrari", "lamborghini", "delorean", "koenigsegg"]
        },
        "countries": {
            "easy": ["usa", "austria", "turkey", "hungary", "sweden", "russia"],
            "medium": ["afghanistan", "kazachstan", "turkmenistan", "thailand", "panama"],
            "hard": ["liechtenstein", "kenya", "madagascar", "myanmar", "bangladesh", "nepal"]
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

def play_again():
    while True:
        play_again_input = input("Would you like to play again? (y/n) ").strip().lower()
        if play_again_input in ['y', 'n']:
            return play_again_input == 'y'  
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def play_hangman():
    print("Welcome to Hangman!")
    start_game = input("Press 'y' to start the game: ").strip().lower()
    
    if start_game != 'y':
        return

    category = ""
    while category not in ["foods", "cars", "countries"]:
        category = input("Which category of words would you like to guess (foods/cars/countries)? ").strip().lower()
    
    difficulty = ""
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    
    word = choose_word(category, difficulty)
    word_completion = "_" * len(word)  
    guessed = False  
    guessed_letters = []
    tries = 6
    
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:  # Main game loop
        guess = input("Please guess a letter: ").lower()
        
        if len(guess) == 1 and guess.isalpha(): # Validate input
            if guess in guessed_letters:
                print("You already guessed", guess) # Repeat guess message
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess) # Track guessed letter
                print("Guessed Letters:", guessed_letters)
                print("Remaining tries:", tries)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion) # Convert to list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess # Update guessed letters
                word_completion = "".join(word_as_list) # Convert back to string
                if "_" not in word_completion:
                    guessed = True

        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

    return play_again()

if __name__ == "__main__":
    while play_hangman():
        pass
    print("Thank you for playing, have a nice day!")
