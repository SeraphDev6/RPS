
#play the game
def play(player_1,player_2,number_of_games,print_games=False):
    #set up begining parameters
    player_1_prev_play=""
    player_2_prev_play=""
    results={"p1":0 , "p2":0, "tie":0}
    #loop through all the games
    for _ in range(number_of_games):
        #run each player's algorithm and give it each others previous play
        p1_play =player_1(player_2_prev_play)
        p2_play =player_2(player_1_prev_play)
        #check who wins
        if p1_play==p2_play:
            results["tie"]+=1
            winner="tie"
        elif (p1_play=="R" and p2_play=="S") or (p1_play=="S" and p2_play=="P")or (p1_play=="P" and p2_play=="R"):
            results["p1"]+=1
            winner="Player 1 Wins"
        elif (p1_play=="P" and p2_play=="S") or (p1_play=="R" and p2_play=="P")or (p1_play=="S" and p2_play=="R"):
            results["p2"]+=1
            winner="Player 2 Wins"
        #Print Games if selected
        if print_games:
            print(f"Player 1: {p1_play} Player 2: {p2_play}")
            print(winner)
            print()
        #Return the Previous Play for each player's data
        player_1_prev_play=p1_play
        player_2_prev_play=p2_play
    #print the final results for each player
    games_won=results["p1"]+results["p2"]
    if games_won > 0:
        p1_percent = results["p1"]/games_won*100
        p2_percent = results["p2"]/games_won*100
        print(results)
        print(f"Player 1 won {p1_percent}% of games")
        print(f"Player 2 won {p2_percent}% of games")
        if p1_percent == p2_percent:
            print("It's a Tie!")
        elif p1_percent > p2_percent:
            print("Player 1 wins!!")
        elif p1_percent < p2_percent:
            print("Player 2 wins!!")
    else:
        print("All of the Games were ties....")
        
        
        
