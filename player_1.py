import random
#make the play function
def play1(previous_play,play_history=[]):
    #keep track of opponent's plays
    play_history.append(previous_play)
    #make an array of Play options
    play_options=["R","P","S"]
    #use information gathered to make a strategic choice
    #---------------------------------------------------
    #put smart people code here
    #---------------------------------------------------

    #or just pick randomly
    return play_options[random.randint(0,2)]
