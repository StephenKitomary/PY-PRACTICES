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
        
    if final_choice[0] == prize:
        pass
        #print("You win!")
    else:
        pass
        #print("You lose!")
    Game_stats = {'prize_door': prize, 'initial_choice': user_choice, 'revealed_door':revealed_door[0], 'final_choice': final_choice[0]}
    return Game_stats

print(play_game(True))
