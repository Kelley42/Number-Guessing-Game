from art import logo
import random
import os

def play_game():
    game = True
    print(logo)
    number = random.randint(1, 100)
    while True:
        difficulty_level = input("\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_level == 'easy':
            attempts = 10
            break
        elif difficulty_level == 'hard':
            attempts = 5
            break
        else:
            print("\nIncorrect response - please try again.")
    guessed_correct = False
    while guessed_correct == False:
        if attempts == 0:
            print(f"\nYou lose. The number was {number}.")
            play_again()
        else:
            while attempts > 0:
                while True:
                    try:
                        number_guess = int(input(f"\nYou have {attempts} attempts remaining to guess the number.\nMake a guess: "))
                    except ValueError:
                        print("\nGuess must be an integer - try again.")
                    else:
                        break
                if number_guess == number:
                    guessed_correct == True
                    print(f"\nYou got it! The answer was {number}.")
                    play_again()
                elif number_guess > number:
                    print("\nToo high.\nGuess again.")
                    attempts -= 1
                elif number_guess < number:
                    print("\nToo low.\nGuess again.")
                    attempts -= 1

def play_again():
    while True:
        play_again_input = input("\nDo you want to play again? 'y' or 'n': ").lower()
        if play_again_input == 'n':
            game = False
            exit()
        elif play_again_input == 'y':
            os.system('clear')
            play_game()
        else:
            print("Incorrect answer - please try again.")

play_game()
    
