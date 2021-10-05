import random

Words_list = ["Balloon" , "Window"]

main_word = random.choice(Words_list).lower()

guessed_letter = input("Enter a letter:\t").lower()

main_words_blanks = ["_" for letter in main_word]

for letter in range(len(main_word)): 
    if main_word[letter] == guessed_letter:
        main_words_blanks[letter] = guessed_letter
        
        
print(main_words_blanks)