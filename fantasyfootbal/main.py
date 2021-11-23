# !!!!!!!!!!!!!!!!!!!!! you have appended SCORE !!!!!!!!!!!!!!!!!!!!!!
from math import floor


def for_all_players(player_data):
    score = int(player_data.pop(-1))
    if int(player_data[2]) >= 60:  # minutes_played
        score += 2
    if int(player_data[2]) < 60:
        score += 1
    # number_of_assists #numbers_of_yellow #numbers_of_red #number_of_own_goals
    score = score + ((int(player_data[4]) * 3) +
                     (int(player_data[-4]) * -1) +
                     (int(player_data[-3]) * -3))

    player_data.append(score)


def GKP(player_data):
    for_all_players(player_data)
    score = int(player_data.pop(-1))

    if int(player_data[5]) == 0:
        score += 4

    elif int(player_data[5]) % 2 == 0:
        score -= (int(player_data[5])/2)
    else:
        score -= floor(int(player_data[5])/2)

    if int(player_data[6]) % 3 == 0:
        score += (int(player_data[6])/3)
    else:
        score += floor(int(player_data[6])/3)

    score = score + (
        int(player_data[3]) +
        (int(player_data[7]) * 5) +
        (int(player_data[8]) * -2) +
        (int(player_data[-2]) * -2)
    )
    player_data.append(score)


def DEF(player_data):
    for_all_players(player_data)
    score = int(player_data.pop(-1))

    if int(player_data[5]) == 0:
        score += 4
    # elif int(player_data[5]) != 0:
    #     score -= floor(int(player_data[5])/2)

    score = score + (
        (int(player_data[4]) * 6)
    )

    player_data.append(score)


def MID(player_data):
    for_all_players(player_data)
    score = int(player_data.pop(-1))



all_data = []
while True:
    try:
        all_data.append(input()) # Or whatever prompt you prefer to use.
    except EOFError:
        break

friends_list = [data.split() for data in all_data]
all_score = 0

for player in friends_list:
    player.append(all_score)
    if player[1] == "GKP":
        GKP(player)
    elif player[1] == "DEF":
        DEF(player)
    print(player)

