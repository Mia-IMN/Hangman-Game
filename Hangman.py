import random
from Hangman_art import welcome_image, HANGMANPICS
from Hangman_wordlist import easy_word_dictionary, medium_word_list, hard_word_list

final_score = 0

def play_game():

    # scoring system - each try would minus 10 marks out of 100 for easy, 150 for medium and 200 for hard
    # fix easy not starting the game
    print(welcome_image)

    # code that let's player choose difficulty level
    level_difficulty = input("Choose difficulty level: E (Easy) || M (Medium) || H (Hard) \n")

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

        global final_score
        
        if level == "easy":
            score = 100
            print(f"Current score = {final_score}")
            print("Max score after each word guess: 100")
            print("\n************* Start!! *************\n")
        elif level == "medium":
            score = 150
            print(f"Current score = {final_score}")
            print("Max score after each word guess: 150")
            print("\n************* Start!! *************\n")
        elif level == "hard":
            score = 200
            print(f"Current score = {final_score}")
            print("Max score after each word guess: 200")
            print("\n************* Start!! *************\n")

        # Used these to control the printshow_update function later on
        easy = False
        medium = False
        hard = False

        want_hint = False

        guesses_list = []

        # Picks which word list to use based on the user's choice level 
        if level == "easy":
            current_pick = random.choice(list(easy_word_dictionary.keys())).lower()
            show_update = ["_ ", "_ ", "_"]
            printshow_update(3, show_update)
            easy = True

        if level == "medium":
            current_pick = random.choice(medium_word_list).lower()
            show_update = ["_ ", "_ ", "_ ", "_ ", "_ "]
            printshow_update(5, show_update)
            medium = True

        if level == "hard":
            current_pick = random.choice(hard_word_list).lower()
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

            # To check if the user guessed a letter they had already guessed
            if user_guess not in guesses_list:
                guesses_list.append(user_guess)
            else:
                print("\nYou've already guessed this letter!\n")
                should_break = True


            for serial in current_pick:

                if should_break == True:
                    continue
                            
                elif user_guess == serial:
                    show_update[update_num] = serial
                    mini_count += 1

                update_num += 1

            count += mini_count
            
            if should_break == False:
                if easy == True:
                    printshow_update(3, show_update, "-------> ")
                if medium == True:
                    printshow_update(5, show_update, "-------> ")
                if hard == True:
                    printshow_update(7, show_update, "-------> ")

                if mini_count > 0:
                    if count == check_len:
                        print("\n\n************* You win!! *************")
                        print(f"********** Score = {score} points *************\n")
                        final_score += score
                        print("Do you want to try again? (y/n): ", end="")
                        another_try = input().lower()
                        if another_try == 'y':
                            play_game()
                        elif another_try == 'n':
                            print("\n************* Game Over!! *************")
                            print(f"******* Final Score = {final_score} points *****\n")
                        else: 
                            print("\n~~~~~~~~~~~~~ Wrong Input!! ~~~~~~~~~~~~~\n")
                            print("\n************** Game Over!! *************")
                            print(f"***** Final Score = {final_score} points *****\n")
                    else:
                        print("\n\n~~~~ Nice!! ~~~~")
                        print("Execution paused :)")
                        print(HANGMANPICS[6 - tries])
                else:
                    tries -= 1
                    print("\n\nOops... that letter isn't in the word")
                    print(HANGMANPICS[6 - tries])
                    score -= 10
                    if tries > 0:
                        print(f"~~~~~~~~~~~~~~~~~ -10 points ~~~~~~~~~~~~~")
                        print(f"~~~~~~~~~~~~~ {tries} tries remaining ~~~~~~~~~~~~~")
                        if tries <= 2:
                            if final_score > 0:
                                print("\nHint cost -20 points")
                                hint = input("Want a hint? (y/n): ")
                                if hint == "y":
                                    print(easy_word_dictionary[current_pick])
                                    final_score -= 20
                    if tries == 0:
                        print(f"\nCorrect Word = {current_pick}")
                        print("\n************* You lose!! *************")
                        print(f"*********** Score = 0 points ***********\n")
                        print("Do you want to play again? (y/n): ", end="")
                        another_try = input().lower()
                        if another_try == 'y':
                            play_game()
                        elif another_try == 'n':
                            print("\n************* Game Over!! *************")
                            print(f"***** Final Score = {final_score} points *****\n")
                        else: 
                            print("\n************* Wrong Input!! *************\n")
                            print("\n************** Game Over!! *************")
                            print(f"***** Final Score = {final_score} points *****\n")
            
            if tries > 0 and not count == check_len:
                print("\nGuess another letter: ", end="")
            
    
    # Block of code that handles game's difficulty level
    if level_difficulty.lower() == "h":
        print("\nDifficulty level set to Hard!\nYou get to guess 7 letter words in 6 trials\n")
        play("hard")
    elif level_difficulty.lower() == "m":
        print("\nDifficulty level set to Medium!\nYou get to guess 5 letter words in 6 trials\n")
        play("medium")
    elif level_difficulty.lower() == "e":
        print("\nDifficulty level set to Easy!\nYou get to guess 3 letter words in 6 trials\n")
        play("easy")
    else:
        print("Please choose an option from the list", end="")
        play_game()

play_game()