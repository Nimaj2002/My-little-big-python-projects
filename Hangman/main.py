import random
import art

Words_list = ["Balloon" , "Window"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

main_word = random.choice(Words_list).lower()
main_words_blanks = ["_" for letter in main_word]

health = 6
end_of_game = False

print(art.logo)
print("Welcome to Hangman Game!")
print(f" {' '.join(main_words_blanks)} ")

while not end_of_game and health>0:
    guessed_letter = input("Guess a letter:\t").lower()
    
    if guessed_letter in main_word:
        for letter in range(len(main_word)): 
            if main_word[letter] == guessed_letter:
                main_words_blanks[letter] = guessed_letter
        print(stages[health])      
                
    elif not guessed_letter in main_word:
        health -= 1
        print(stages[health])
        
    print(f" {' '.join(main_words_blanks)} ")
    
    if "_" not in main_words_blanks:
        end_of_game = True
        print("You won")
        
    elif health == 0 and not end_of_game:
        end_of_game = True
        print("You loss")
