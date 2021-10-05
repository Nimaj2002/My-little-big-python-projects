import random

Words_list = ["Balloon" , "Window"]

main_word = random.choice(Words_list).lower()
main_word_letters = []
print(main_word)

for letter in main_word:
    main_word_letters.append(letter)

main_words_blanks = ["_" for letter in main_word]

while main_word_letters != main_words_blanks:
    guessed_letter = input("Enter a letter:\t").lower()

    for letter in range(len(main_word)): 
        if main_word[letter] == guessed_letter:
            main_words_blanks[letter] = guessed_letter
    print(main_words_blanks)

if main_word_letters == main_words_blanks:
    print("You won")