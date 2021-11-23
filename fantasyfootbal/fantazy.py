# from math import floor
def floor(x):
    d = x % 1
    x = x - d
    return x


def GKP(player_data):
    score = int(player_data.pop(-1))

    if 60 <= int(player_data[2]) <= 90:  # minutes_played
        score += 2
    if 1 <= int(player_data[2]) < 60:
        score += 1

    if int(player_data[5]) == 0:  # clean shit
        score += 4
    elif int(player_data[5]) != 0:  # every two goals
        score -= floor(int(player_data[5]) / 2)

    score += (
            (int(player_data[3]) * 6) +
            (int(player_data[4]) * 3) +
            floor(int(player_data[6]) / 3) +
            (int(player_data[7]) * 5) +
            (int(player_data[8]) * -2) +
            (int(player_data[9]) * -1) +
            (int(player_data[10]) * -3) +
            (int(player_data[11]) * -3)
    )

    player_data.append(score)


def DEF(player_data):
    score = int(player_data.pop(-1))

    if 60 <= int(player_data[2]) <= 90:  # minutes_played
        score += 2
    if 1 <= int(player_data[2]) < 60:
        score += 1

    if int(player_data[5]) == 0:  # clean shit
        score += 4
    elif int(player_data[5]) != 0:  # every two goals
        score -= floor(int(player_data[5]) / 2)

    score += (
            (int(player_data[3]) * 6) +
            (int(player_data[4]) * 3) +
            (int(player_data[6]) * -2) +
            (int(player_data[7]) * -1) +
            (int(player_data[8]) * -3) +
            (int(player_data[9]) * -2)
    )


def MID(player_data):
    score = int(player_data.pop(-1))

    if 60 <= int(player_data[2]) <= 90:  # minutes_played
        score += 2
    if 1 <= int(player_data[2]) < 60:
        score += 1

    if int(player_data[5]) == 0:  # clean shit
        score += 1

    score += (
            (int(player_data[3]) * 5) +
            (int(player_data[4]) * 3) +
            (int(player_data[6]) * -2) +
            (int(player_data[7]) * -1) +
            (int(player_data[8]) * -3) +
            (int(player_data[9]) * -2)
    )

    player_data.append(score)


def FWD(player_data):
    score = int(player_data.pop(-1))

    if 60 <= int(player_data[2]) <= 90:  # minutes_played
        score += 2
    if 1 <= int(player_data[2]) < 60:
        score += 1

    score += (
            (int(player_data[3]) * 4) +
            (int(player_data[4]) * 3) +
            (int(player_data[5]) * -2) +
            (int(player_data[6]) * -1) +
            (int(player_data[7]) * -3) +
            (int(player_data[8]) * -2)
    )

    player_data.append(score)


# ----------------------------------------------------------------------#


all_data = []
while True:
    try:
        all_data.append(input())
    except EOFError:
        break

while all_data[-1] == "":
    all_data.pop(-1)

players_list = [data.split() for data in all_data]
all_score = 0

for player in players_list:
    player.append(all_score)
    if player[1] == "GKP":
        GKP(player)
    elif player[1] == "DEF":
        DEF(player)
    elif player[1] == "MID":
        MID(player)
    elif player[1] == "FWD":
        FWD(player)

max_score = 0
for player in players_list:
    if int(player[-1]) > max_score:
        max_score = int(player[-1])

for player in players_list:
    if int(player[-1]) == max_score:
        print(player[0])
