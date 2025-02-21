""" Simulate the problem with 3 doors.  Conduct 10,000 rounds of switching, and 10,000 rounds of not switching.
Define play_game(switch_strategy), where:
The formal parameter switch_strategy is a boolean determining whether you are a switcher or a stayer.
A dictionary with the following keys and corresponding values are returned: 'prize_door', 'initial_choice', 'revealed_door', 'final_choice' """
import random


def  play_game(switch_strategy):
    user_choice = random.randint(1, 3)
    #print("user_choice:",user_choice)
    prize = random.randint(1, 3)
    #print("Prize door", prize)
    choices = {1, 2, 3}
    user = {user_choice,prize}
    revealed_door = list(choices.difference(user))
    #print("revelaed_door:",revealed_door[0])
    final_choice = [1,]
    if switch_strategy:
        final_choice = list(choices.difference({user_choice, revealed_door[0]}))
    

    else:
        final_choice[0] = user_choice
    #print("final choice:", final_choice[0])
    Game_stats = {'prize_door': prize, 'initial_choice': user_choice, 'revealed_door':revealed_door[0], 'final_choice': final_choice[0]}
    return Game_stats

def run_simulation(num_games):
    switch_wins = 0
    stay_wins = 0
    with open("game_simulation.txt", "w") as file:
        # switch
        for i in range(num_games):
            game = play_game(True)
            if game['final_choice'] == game['prize_door']:
                switch_wins += 1
                outcome = "win"
            else:
                outcome = "loss"
            log_line = f"{game['prize_door']}; {game['initial_choice']}; {game['revealed_door']}; {game['final_choice']}; {outcome}; switch"
            file.write(log_line + "\n")
        
        # stay:
        for i in range(num_games):
            game = play_game(False)
            if game['final_choice'] == game['prize_door']:
                stay_wins += 1
                outcome = "win"
            else:
                outcome = "loss"
            log_line = f"{game['prize_door']}; {game['initial_choice']}; {game['revealed_door']}; {game['final_choice']}; {outcome}; stay"
            file.write(log_line + "\n")
        
    switch_win_rate = (switch_wins / num_games) * 100
    stay_win_rate = (stay_wins / num_games) * 100

    print("Number of games (per strategy):", num_games)
    print("Number of switch wins:", switch_wins)
    print("Number of stay wins:", stay_wins)
    print(f"Switch win rate: {switch_win_rate:.2f}%")
    print(f"Stay win rate: {stay_win_rate:.2f}%")

    
       

run_simulation(10000)