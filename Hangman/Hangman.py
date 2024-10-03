import random

# Welcome Image
print('''
  _    _            _   _   _____  __  __            _   _ 
 | |  | |    /\    | \ | | / ____||  \/  |    /\    | \ | |
 | |__| |   /  \   |  \| || |  __ | \  / |   /  \   |  \| |
 |  __  |  / /\ \  | . ` || | |_ || |\/| |  / /\ \  | . ` |
 | |  | | / ____ \ | |\  || |__| || |  | | / ____ \ | |\  |
 |_|  |_|/_/    \_\|_| \_| \_____||_|  |_|/_/    \_\|_| \_|
                                                           
                                                           
      ''')

# Hangman Images
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# word list for various difficulty level
easy_word_list = ["cat", "man", "boy", "toy", "fix", "lie", "coy", "tie", "tye", "cue"]
medium_word_list = ["leave", "weigh", "angry", "minor", "happy", "break", "woman", "begin", "eight", "towel"]
hard_word_list = ["contain", "express", "charity", "twitter", "teacher", "fifteen", "mankind", "keyword", "counter", "builder"]

# code that let's player choose difficulty level
level_difficulty = input("Choose difficulty level: Easy || Medium || Hard\n")


# Play function
def play(level):

    print(HANGMANPICS[0])

    if level == "easy":
        current_pick = random.choice(easy_word_list)
        show_update = ["_ ", "_ ", "_"]
        print(show_update)

    if level == "medium":
        current_pick = random.choice(medium_word_list)
        show_update = ["_ ", "_ ", "_", "_ ", "_ "]
        print(show_update)

    if level == "hard":
        current_pick = random.choice(hard_word_list)
        show_update = ["_ ", "_ ", "_", "_ ", "_ ", "_ ", "_"]
        print(show_update)

    count = 0
    tries = 6
    print('\nGuess a letter: ', end="")
    check_len = len(current_pick)
    
    while (tries > 0) and not (count == check_len):
        update_num = 0
        
        user_guess = input()
        user_guess = user_guess.lower()
        # print(current_pick)
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
        
        print(show_update)
        if mini_count > 0:
            if count == check_len:
                print("\nYou win!!")
            else:
                print("\nYou're on fire!!")
        else:
            tries -= 1
            print(HANGMANPICS[6 - tries])
            print(f"\nYou have {tries} tries remaining")
            if tries == 0:
                print(f"\nCorrect Word = {current_pick}\n")

        if tries > 0 and not count == check_len:
            print("\nGuess another letter: ", end="")
        # print(tries, count)
        

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

