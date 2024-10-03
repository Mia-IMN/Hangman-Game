import random
from Hangman_art import welcome_image, HANGMANPICS
from Hangman_wordlist import easy_word_list, medium_word_list, hard_word_list


print(welcome_image)


# code that let's player choose difficulty level
level_difficulty = input("Choose difficulty level: Easy || Medium || Hard\n")

# show_update is the array that contains the users guesses
# this function reduces ambiguity caused by constant printing of
# the show_update array in different ways.
def printshow_update(number, functn, text = "What could this word be: "):
    print(text, end="")
    for num in range(number):
        print(functn[num], end=" ")
    
# Play function
def play(level):

    print(HANGMANPICS[0])

    # Used these to control the printshow_update function later on
    easy = False
    medium = False
    hard = False

    # Picks which word list to use based on the user's choice level 
    if level == "easy":
        current_pick = random.choice(easy_word_list)
        show_update = ["_ ", "_ ", "_"]
        printshow_update(3, show_update)
        easy = True

    if level == "medium":
        current_pick = random.choice(medium_word_list)
        show_update = ["_ ", "_ ", "_ ", "_ ", "_ "]
        printshow_update(5, show_update)
        medium = True

    if level == "hard":
        current_pick = random.choice(hard_word_list)
        show_update = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_"]
        printshow_update(7, show_update)
        hard = True
    
    # used this to control the following while function as well as to 
    # know if the user has won or lost.
    count = 0
    tries = 6

    print('\nGuess a letter: ', end="")
    
    # Get's the length of the current word pick. I used this to control
    # the following while loop and other conditional statement that depends
    # on the word size
    check_len = len(current_pick)
    
    # Loop function that makes the game repetitive until win or lose
    while (tries > 0) and not (count == check_len):
        update_num = 0
        
        # Used this to get the input and also fix the issue of user using
        # uppercase during the game
        user_guess = input().lower()

        mini_count = 0
        should_break = False

        for one in show_update:
            if user_guess == show_update[show_update.index(one)]:
                print("\nYou've already guessed this letter.\nGuess another!\n")
                should_break = True

        for serial in current_pick:

            if should_break == True:
                continue
                         
            if user_guess == serial:
                show_update[update_num] = serial
                mini_count += 1


            update_num += 1
        count += mini_count
        
        if easy == True:
            printshow_update(3, show_update, "-------> ")
        if medium == True:
            printshow_update(5, show_update, "-------> ")
        if hard == True:
            printshow_update(7, show_update, "-------> ")

        if mini_count > 0:
            if count == check_len:
                print("\n\n************* You win!! *************")
            else:
                print("\n\nWoaw... You're on fire!!")
                print("\nExecution paused :)")
                print(HANGMANPICS[6 - tries])
        else:
            tries -= 1
            print("\n\nOops... that letter isn't in the word")
            print(HANGMANPICS[6 - tries])
            print(f"************* {tries} tries remaining *************")
            if tries == 0:
                print(f"\nCorrect Word = {current_pick}")
                print("\n************* You lose!! *************\n")

        if tries > 0 and not count == check_len:
            print("\nGuess another letter: ", end="")
        

# Block of code that handles game's difficulty level
if level_difficulty.lower() == "hard":
    print("\nDifficulty level set to Hard!\nYou get to guess 7 letter words in 6 trials\n")
    play("hard")
elif level_difficulty.lower() == "medium":
    print("\nDifficulty level set to Medium!\nYou get to guess 5 letter words in 6 trials\n")
    play("medium")
elif level_difficulty.lower() == "easy":
    print("\nDifficulty level set to Easy!\nYou get to guess 3 letter words in 6 trials\n")
    play("easy")
else:
    print("Please choose an option between \"Easy, Medium or Hard\"\n")

