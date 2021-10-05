import random

Words_list = ["Balloon" , "Window"]

main_word = random.choice(Words_list).lower()

quessed_letter = input("Enter a letter:\t").lower()

for letter in main_word:
    if letter == quessed_letter :
        print("True")
    else:
        print("False")

print(main_word)