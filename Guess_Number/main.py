import guess

play = guess.run_game()
while play  == True:
    ask = input("Do you want to play again? Y or N\n").upper()
    if ask == "Y":
        play = guess.run_game()
    else:
        play = False