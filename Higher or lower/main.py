import random
import art
from game_data import data

####################################################################################################

print(art.logo)


####################################################################################################
def win_check(a_or_b):
    if a_or_b == "A" and data_A_follower_count > data_B_follower_count:
        return True
    elif a_or_b == "B" and data_A_follower_count < data_B_follower_count:
        return True
    else:
        return False


def generate_data(data_b):
    if not USER_WIN:
        a_number = random.randint(0, len(data))
        data_a = data.pop(a_number)
        data_a_follower_count = data_a['follower_count']
        print(f"Compare A: {data_a['name']} , {data_a['description']} , from {data_a['country']}")

        print(art.vs)

        b_number = random.randint(0, len(data) - 1)
        data_b = data.pop(b_number)
        data_b_follower_count = data_b['follower_count']
        print(f"Compare B: {data_b['name']} , {data_b['description']} , from {data_b['country']}")

        return data_b, data_a_follower_count, data_b_follower_count

    elif USER_WIN:
        data_a = data_b
        data_a_follower_count = data_a['follower_count']
        print(f"Compare A: {data_a['name']} , {data_a['description']} , from {data_a['country']}")

        print(art.vs)

        b_number = random.randint(0, len(data) - 1)
        data_b = data.pop(b_number)
        data_b_follower_count = data_b['follower_count']
        print(f"Compare B: {data_b['name']} , {data_b['description']} , from {data_b['country']}")

        return data_b, data_a_follower_count, data_b_follower_count


####################################################################################################
game_is_finished = False
USER_WIN = False
data_B = {}
score = 0
while not game_is_finished:
    data_B, data_A_follower_count, data_B_follower_count = generate_data(data_B)
    A_or_B = input("Who has more followers? Type 'A' or 'B':\t").upper()

    if win_check(A_or_B):
        score += 1
        print(f"You're right! Current score: {score}")
        USER_WIN = True
    elif not win_check(A_or_B):
        print(f"You loose! Better Luck next time! Your score was {score}")
        game_is_finished = True
