import blackjack


play = blackjack.run_game()
while play  == True:
    ask = input("Do you want to play again? Y or N\n").upper()
    if ask == "Y":
        play = blackjack.run_game()
    else:
        play = False
