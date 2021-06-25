import random
#make the play function
def play1(previous_play,play_history=[],last_play=""):
    #keep track of opponent's plays
    play_history.append(previous_play)
    #how many times we lost in a row(ties dont reset)
    losses_in_a_row=0
    #make an array of Play options
    play_options=["R","P","S"]
    counters={"R":"P","P":"S","S":"R"}
    
    #use information gathered to make a strategic choice
    #---------------------------------------------------
    #put smart people code here
    #check if we win or lose
    if previous_play != "" and last_play!="":
        if counters[previous_play]==last_play:
            losses_in_a_row+=1
        elif counters[last_play]==previous_play:
            losses_in_a_row=0
    #without enough data just play randomly
    if len(play_history)>3:
        #if we are on a winning streak keep using that strategy
        if losses_in_a_row<=3:
            last_play=counters[play_history[len(play_history)-2]]
            return last_play
        else:
            last_play=play_options[random.randint(0,2)]
            return last_play
        
    #---------------------------------------------------

    #or just pick randomly
    last_play=play_options[random.randint(0,2)]
    return last_play
