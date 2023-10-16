# Hangman-game
This Python-based Hangman game enables users to guess words, categorized into different topics and difficulty levels, by iteratively selecting letters, while visually tracking incorrect guesses through ASCII hangman illustrations.

# Overview
  ## Project
   The game starts with the games logo and a welcome introduction and explanation of the game.

   The Hangman game provides a word-guessing experience where a player selects a category and difficulty level, then has to identify a hidden word by suggesting letters. A partial hangman figure gets drawn with each incorrect guess, and the player is allowed up to 6 mistakes. Displayed underscores signify the word length, and a list assists in tracking previously guessed letters.
   
   The Player wins if he guesses the word before the hangman is fully drawn; otherwise, the correct word is revealed upon loss. The Player then can choose to play again or exit the game.

# Game Structure

## Start Screen
- **Logo and Welcome:** A symbol-created logo is displayed along with a welcoming message.
- **Instructions:** Provides easy-to-understand instructions for how to play.
- **Game Initiation:** Player begins the game by pressing 'y'.

## Category and Difficulty Selection
- **Category Choice:** Player selects a word category (foods, cars, countries).
- **Difficulty Choice:** Player selects a difficulty level (easy, medium, hard).

## Input Validation
- **Correct Input:** Ensures the player’s input adheres to acceptable parameters (e.g., 'y' to start, valid category, and difficulty).
- **Error Messaging:** Informative error messages guide the player towards valid inputs.

## Main Game 
- **Word Representation:** Displays underscores (_) representing the secret word's letters.
- **Letter Guessing:** Player attempts to reveal the word by guessing letters one at a time.
- **Hangman Figure:** Incorrect guesses visually build a hangman drawing and guessess become less.
- **Guessed Letters:** Displays a list to track and show letters the player has already guessed.

## End of Round
- **Outcome:** Reveals whether the player won or lost and shows the correct word.
- **Replay Option:** Presents the player with the choice to play again or exit.

## Potential future updates
 Future updates for the Hangman game include better player experience through expanded and customizable word categories, the addition of user profiles and competitive leaderboards, along with a notable uplift in graphical and user interaction, moving from ASCII to a more vibrant and intuitive UI/UX.

# Class-Based Data Model

The game consists of 3 main classes, `WordManager`, `GameManager` and `play_hangman()` . These 2 classes create the base structure of the game mechanics.

### Class 1: `WordManager`
**Responsibility:** Manages word retrieval and masking based on player choices.

#### Attributes:
- `categories`: Available word categories.
- `difficulties`: Available difficulty levels.

#### Methods:
- `get_word(category, difficulty)`: Retrieves a word matching player preferences.
- `mask_word(word, guessed_letters)`: Masks the word, revealing guessed letters.

### Class 2: `GameManager`
**Responsibility:** Manages gameplay logic, status updates, and user interactions.

#### Attributes:
- `max_attempts`: Maximum incorrect guesses allowed.
- `guessed_letters`: Letters guessed by the player.
- `incorrect_attempts`: Number of incorrect guesses.

#### Methods:
- `get_guess()`: Obtains and validates player's letter guess.
- `update_game_status(guessed_letter)`: Updates gameplay variables based on recent guess.
- `display_status()`: Showcases the current gameplay status.
- `display_outcome()`: Informs player of the round’s outcome.

#### Methods:
- `print_logo_and_explanation()`: Displays the game logo and instructions.
- `select_category()`: Prompts and validates category selection.
- `select_difficulty()`: Prompts and validates difficulty selection.
- `replay_prompt()`: Asks the player if they wish to play again.

## Main Loop: `play_hangman()`
In an object-oriented adaptation, the main loop could instantiate objects of these classes and coordinate their methods to facilitate the gameplay. It initiates game start, loops through player guesses while managing game status, and concludes the round, potentially looping into a new game or ending as per player input.

# Testing

## Validator Testing


# Hangman Game - Manual Testing

## **Test Scenario 1: Start the Game**

### Test Steps:
1. Execute the program.
2. Prompted to press 'y' to start the game.

### Test Input:
- `y`

### Results:
- Hangman logo and game explanation displayed.
- Prompt to press 'y' to start the game appeared.
- Successful transition to category selection.

---

## **Test Scenario 2: Category Selection**

### Test Steps:
1. Prompted to select a category (foods/cars/countries).

### Test Input:
- `foods`

### Results:
- Successful transition to difficulty selection.

### Test Input:
- `games`

### Results:
- Error message displayed: "Error Message: Please choose foods, cars, or countries."

---

## **Test Scenario 3: Difficulty Selection**

### Test Steps:
1. Prompted to choose word difficulty (easy, medium, hard).

### Test Input:
- `easy`

### Results:
- Successful transition to main game loop.

### Test Input:
- `extreme`

### Results:
- Error message displayed: "Error Message: Please choose easy, medium, or hard."

---

## **Test Scenario 4: Guess a Letter**

### Test Steps:
1. Prompted to guess a letter.
2. Enter a valid letter.
3. Enter an invalid character.
4. Enter multiple letters.

### Test Input:
1. `a`
2. `9`
3. `ab`

### Results:
1. Feedback displayed depending on whether the letter is in the word.
2. Error message displayed: "Error: Only letters allowed"
3. Error message displayed: "Error: Only one letter a time allowed"

---

## **Test Scenario 5: Guess the Entire Word**

### Test Steps:
1. Continue guessing letters until the word is completed or all attempts are used up.

### Results:
- Upon guessing the entire word correctly, a congratulatory message is displayed.
- Upon using up all attempts without guessing the word, a message with the correct word and encouragement to try again is displayed.

---

## **Test Scenario 6: Play Again**

### Test Steps:
1. After a game finishes, player is prompted to play again.
2. Choose to play again.
3. Choose not to play again.

### Test Input:
1. `y`
2. `n`

### Results:
1. Restarted the game.
2. Displayed the message: "Thank you for playing, have a nice day! ┏( ͡ᵔ _⦣ ͡ᵔ)┛ "

### Test Input:

1. r

### Results:
1. Displayed the message: "Invalid input. Please enter 'y' or 'n'."
---

## **Conclusion**:
The game mostly functions as expected, and the majority of user interactions are handled correctly. Error handling seems to be effective for the inputs tested. 

# Technologies

- Languages: 
  - Python
- Platform: 
  - Heroku

  
# Bugs
### Problem:
When the player was asked to enter "y" to start the game the game kept looping the same question over and over.

### Solution:

Add != instead of === to while_start_game inside the play_hangman() function.

# Credits 

- [FreeCodeCamp](https://www.freecodecamp.org/) showcased how to use Data Structures (dictionaries and lists), and also how to correctly manipulate strings (like .lower() and .strip() )

- [Reddit](https://https://www.reddit.com/r/Python/) this subreddit has been a big help in explaining to me Modular Programming for my project.

- [Fsymbols](https://fsymbols.com/generators/) great tool for creating the temporary game logo.

[Back to Top](#)





