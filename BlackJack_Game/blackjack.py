import random
import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

######################################################################################################################

def calculate_score(decks_cards):
    sumit = sum(decks_cards)
    if 11 in decks_cards and sumit > 21 :
        decks_cards[decks_cards.index(11)] = 1    
    sumit = sum(decks_cards)
    if sumit == 21 and len(decks_cards) == 2:
        return 0
    else:
        return sumit
    
def deal_card(decks_cards):
    add_card_to_deck = cards[random.randint(0,12)]
    decks_cards.append(add_card_to_deck)
    return decks_cards   


def blackjack(user_cards , computer_cards , game_is_finished):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)    
    if user_score == 0 and computer_score != 0:
        print(f"You Won for BlackJack!\nand Your cards were {user_cards} and dealers cards were {computer_cards}")
        game_is_finished = True
    elif computer_score == 0 or user_score == 0:
        print(f"You Loss for BlackJack!\nand Your cards were {user_cards} and dealers cards were {computer_cards}")
        game_is_finished = True
    else:
        game_is_finished = False
        
    return game_is_finished
    
    
def compare(user_cards , computer_cards , game_is_finished):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if (user_score == computer_score) and not (user_score == computer_score == 21):
        print(f"DRAW!\nand Your cards were {user_cards} and dealers cards were {computer_cards}")
        game_is_finished = True
    elif user_score > 21 :
        print(f"You Loss!\nand Your cards were {user_cards} and dealers cards were {computer_cards}")
        game_is_finished = True
    elif computer_score > 21 :
        print(f"You Won!\nand Your cards were {user_cards} and dealers cards were {computer_cards}")
        game_is_finished = True
    elif user_score > computer_score:
        print(f"You Won!\nand Your cards were {user_cards} and dealers cards were {computer_cards}")
        game_is_finished = True 
    elif user_score < computer_score:
        print(f"You Loss!\nand Your cards were {user_cards} and dealers cards were {computer_cards}")
        game_is_finished = True        
    else:
        game_is_finished = blackjack(user_cards, computer_cards, game_is_finished)
    return game_is_finished    

######################################################################################################################
def run_game():
    print(art.logo)
        
    user_cards = [cards[random.randint(0,12)] for x in range(0,2)]                                                                                                                   #USER PART                   #   
                                                                                                                    
                                                                                                                    
    computer_cards = [cards[random.randint(0,12)] for x in range(0,2)]                                                                                                              #COMPUTER PART               # 
    
    game_is_finished = False
    
                  ##########################################################
    
    print(f"Your first two cards are {user_cards} and Your score {calculate_score(user_cards)} \n and computer's first card is {computer_cards[0]}")
    
    if game_is_finished == False:
        game_is_finished = blackjack(user_cards , computer_cards , game_is_finished)
    
    
    
                  ##########################################################
    
    while game_is_finished == False:
        hit_or_stand = input("Do you want to hit or stand?\n").lower()
        if hit_or_stand == "hit":
            user_cards = deal_card(user_cards)
            print(f"Your cards : {user_cards} , Your score {calculate_score(user_cards)}")
            game_is_finished == False
        if hit_or_stand == "stand":
            while calculate_score(computer_cards) < 17:
                computer_cards = deal_card(computer_cards)
            game_is_finished = compare(user_cards , computer_cards , game_is_finished)

    return game_is_finished       





