import random
last_play=""
losses_in_a_row=0
#make the play function
def play1(previous_play, play_history=[],strategy=[0],nueral_data=[{
  "RRR":0,
  "RRP":0,
  "RRS":0,
  "RPR":0,
  "RPP":0,
  "RPS":0,
  "RSR":0,
  "RSP":0,
  "RSS":0,
  "PRR":0,
  "PRP":0,
  "PRS":0,
  "PPR":0,
  "PPP":0,
  "PPS":0,
  "PSR":0,
  "PSP":0,
  "PSS":0,
  "SRR":0,
  "SRP":0,
  "SRS":0,
  "SPR":0,
  "SPP":0,
  "SPS":0,
  "SSR":0,
  "SSP":0,
  "SSS":0,
}]):
    #keep track of opponent's plays
    play_history.append(previous_play)
    #make an array of Play options
    play_options=["R","P","S"]
    counters={"R":"P","P":"S","S":"R"}
    
    #use information gathered to make a strategic choice
    #---------------------------------------------------
    #put smart people code here
    #without enough data just play randomly
    if len(play_history)>3:
        #if we are on a winning streak keep using that strategy
        pattern="".join(play_history[-3:])
        nueral_data[0][pattern]+=1

        next_plays=[
            "".join(play_history[-2:])+"R",
        "".join(play_history[-2:])+"P",
        "".join(play_history[-2:])+"S"]

        times_played = {
            check: nueral_data[0][check]
            for check in next_plays if check in nueral_data[0]}
        guess= max(times_played, key=times_played.get)[-1:]
        return counters[guess]
    #---------------------------------------------------

    #or just pick randomly
    return play_options[random.randint(0,2)]
