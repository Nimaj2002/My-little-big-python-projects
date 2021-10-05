import random

Words_list = ["Balloon" , "Window"]

main_word = random.choice(Words_list).lower()

main_words_blanks = ["_" for letter in main_word]

end_of_game = False

while not end_of_game:
    guessed_letter = input("Enter a letter:\t").lower()

    for letter in range(len(main_word)): 
        if main_word[letter] == guessed_letter:
            main_words_blanks[letter] = guessed_letter
    print(main_words_blanks)
    
    if "_" not in main_words_blanks:
        end_of_game = True
    
print("You won!")
