import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

# Prints logo from hangman_art.py file 

print(logo)

lives = 6


chosen_word = random.choice(word_list) # Chooses random word from hangman_words.py
print(chosen_word)

# Prints out underscore for the amount of letters in the chosen word.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False # Set a starting condition for while loop.
correct_letters = [] # Empty list for correctly guessed letters
previous_guess = [] # Empty list for previously guess letters

while not game_over: # While the game is not over

    print("****************************<???>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower() # Prompt the user to guess a letter

 

    display = "" # Set an empty string so that the program can fill in the value with either correct or incorrect guess


    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(guess) # If the guessed letter is correct, add it to the correct_letters list
        elif letter in correct_letters:
            display += letter # Also add the correct letter guess to the display variable
        else:
            display += "_" # Put an underscore in place of the unguessed letters

    print("Word to guess: " + display)

# If the guessed letter is not in the word, subtract 1 from the lives variable and add the incorrectly guessed letter to the previous_guess list.
    if guess not in chosen_word:
        lives -= 1
        previous_guess.append(guess)
        print("You have already guessed " + previous_guess[-1])

# If the lives variable reaches a value of 0, the game_over value becomes True and breaks the while loop.
        if lives == 0:
            game_over = True

            
            print(f"***********************YOU LOSE**********************")
# If there are no longer any underscores in the display, then the user wins.
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
# Use the integer value in lives to index the corresponding image in the stages variable
    print(stages[lives])
