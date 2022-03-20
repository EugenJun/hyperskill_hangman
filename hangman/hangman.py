import random


def game():
    print('H A N G M A N')

    while True:
        user_input = input('\nType "play" to play the game, "exit" to quit: ')
        if user_input == 'play':
            start_game()
        elif user_input == 'exit':
            break
        else:
            continue


def start_game():
    words = ["python", "java", "kotlin", "javascript"]
    computers_choice = random.choice(words)
    word_for_printing = ['-' for _ in computers_choice]
    guessed_indices = []
    guessed_letters = []
    counter = 0

    while True:

        if '-' not in word_for_printing:
            print(f"You guessed the word {computers_choice}!\nYou survived!")
            break

        print('\n' + ''.join(c for c in word_for_printing))

        if counter == 8 and '-' in word_for_printing:
            print("You lost!")
            break

        user_input = input("Input a letter: ")

        if len(user_input) != 1:
            print("You should input a single letter")
            continue
        if not user_input.isalpha() or not user_input.islower():
            print("Please enter a lowercase English letter")
            continue
        if (user_input in computers_choice and user_input in guessed_letters) \
                or (user_input not in computers_choice and user_input in guessed_letters):
            print("You've already guessed this letter")
            continue
        if user_input in computers_choice and user_input not in guessed_letters:
            guessed_indexes = [guessed_indices.append(i) for i, c
                               in enumerate(computers_choice) if c == user_input]
            for index in guessed_indices:
                word_for_printing[index] = list(computers_choice)[index]
                guessed_letters.append(user_input)
                continue
        else:
            counter += 1
            if counter == 8:
                print("That letter doesn't appear in the word\nYou lost!")
                break
            else:
                print("That letter doesn't appear in the word")
                guessed_letters.append(user_input)
                continue


game()
