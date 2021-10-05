import random
import art

def run_game():
    print(art.logo)
    print("Welcome to Number Guessing Game!")
    print("Im thinking of a number between 1 and 100.")
    difficulty = input("Choose your difficulty, 'easy' for 10 attempts and 'hard' for 5 attempts:\n").lower()
    
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    
    print(f"You have {lives} attempts to guess the number")
    
    COMPUTER_RANDOM_NUMBER = random.randint(1,101)
    
    game_is_finished = False
    while not game_is_finished and lives > 0:
        guessed_number = int(input("Guess a number:\n"))
        if guessed_number > COMPUTER_RANDOM_NUMBER:
            game_is_finished = False
            lives -= 1        
            print("High")
            print(f"You have {lives} attempts to guess the number")
        elif guessed_number < COMPUTER_RANDOM_NUMBER:
            game_is_finished = False
            lives -= 1
            print("Low")
            print(f"You have {lives} attempts to guess the number")
        elif guessed_number == COMPUTER_RANDOM_NUMBER:
            print("You Won!")
            game_is_finished = True
    if lives == 0:
        print(f"You Lost number was {COMPUTER_RANDOM_NUMBER}")
    return game_is_finished