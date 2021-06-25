import random

def play2(previous_play, play_history=[]):
    play_history.append(previous_play)

    play_options = ["R", "P", "S"]
    counter = {"R": "P", "P": "S", "S": "R"}

    r = 0
    p = 0
    s = 0

    for play in play_history:
        if play == "R":
            r += 1

        elif play == "P":
            p += 1

        else:
            s += 1

    max_played = max(r, p, s)

    if max_played == r:
        random_play = random.randint(1, 2)

    elif max_played == p:
        random_play = random.randint(0, 1) * 2

    else:
        random_play = random.randint(0, 1)

    return counter[play_options[random_play]]
