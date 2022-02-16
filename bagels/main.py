from random import randrange


def bagels(first_num, second_num):
    first_num = str(first_num)
    second_num = str(second_num)
    result = ""
    for digit in range(len(first_num)):
        if first_num[digit] in second_num and first_num[digit] == second_num[digit]:
            result += "Fermi "
        elif first_num[digit] in second_num:
            result += "Pico "
    if result == "":
        result = "Bagels"
    elif result == "Fermi Fermi Fermi ":
        result = "won"
    return result


def start_game():
    print("Bagels, a deductive logic game.\n")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print(f"when I say:{5 * ' '}That means:")
    print(f"{3 * ' '}Pico{9 * ' '}One digit is correct but in the wrong position")
    print(f"{3 * ' '}Fermi{8 * ' '}One digit is correct and in the right position.")
    print(f"{3 * ' '}Bagels{7 * ' '}No digit is correct.")
    print(f"I have thought up a number.")
    print(f"  You have 10 guesses to get it.")

    app_number = str(randrange(0, 999, 1))
    if len(app_number) < 3:
        app_number = f"{3 - len(app_number) * 0}{app_number}"
#    print(app_number)
    guess_number = 1
    is_finished = False
    play_again = None

    while not is_finished:
        if guess_number >= 10:
            is_finished = True
            print("You failed! :(")
            play_again = input('Do you want to play again? (yes or no):\t').upper()
        else:
            print(f"Guess #{guess_number}")
            user_num = str(input())
            if len(user_num) > 3 or len(user_num) < 3 or user_num.isnumeric() == False:
                print('invalid input!!!')
            else:
                f_result = bagels(app_number, user_num)
                if f_result == "won":
                    is_finished = True
                    print("You got it! :)")
                    play_again = input('Do you want to play again? (yes or no):\t').upper()
                else:
                    print(f_result)
                    guess_number += 1

    return play_again


if __name__ == "__main__":
    run = True
    p_again = "YES"
    while run:
        if p_again == "YES":
            p_again = start_game()
            run = True
        elif p_again == "NO":
            print("Thanks for playing!")
            input("press Any key to exit")
            run = False
        else:
            print('invalid input!!!')
            p_again = input('Do you want to play again? (yes or no):\t').upper()
