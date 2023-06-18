# This file represents the referee of the game.
from agent import *
import create_map
import pandas as pd
import numpy as np
import random
from gui import *


run_test_game()

init_game_map = create_map.initialize_map()
game_map = init_game_map
fig = get_agent_video([go.Frame(data = get_plot(game_map))], init_game_map)

fig.show()

agent_list = get_test_agents()

def initialize_referee():
    
    agents_alive = 8 # defines the number of agents currently playing the game and are not dead
    
    while agents_alive != 1: # while there is no winner do:
        
        find_agents_with_shared_positions_and_teams(agent_list) 
        # call fn check_agent_positions # TODO: Get positions from Kat's code for each class (pass as argument the position attribute of the agent.)


def engagement(combatants):
    # Example lists
    
    for agent in combatants:
        teams = [agent.team_n for agent in combatants]
        powers = [agent.traits['power'] for agent in combatants]

    print("Teams:", teams)
    print("Powers:", powers)
    print("Called function engagement.")
    
    total_power = sum(powers)

    for agent in combatants:
        normalized_powers = [(agent.traits['power'] / total_power) for agent in combatants]
    
    print("Normalized Powers: ",normalized_powers)

    print(agent.traits['power'])

    team_powers = {}
    for team, power in zip(teams, powers):
        if team not in team_powers:
            team_powers[team] = []
        team_powers[team].append(power)

# Create a new list of combined powers for each team
    combined_powers = [sum(powers) for powers in team_powers.values()]
    print("Combined Powers: ", combined_powers)
    winner = random.choices(population=range(len(combined_powers)),weights=combined_powers)
    print("Winner: ", winner)
    [print(f"Killed Agent: {i}") for i, agent in enumerate(combatants) if i != winner[0]]
    


def find_agents_with_shared_positions_and_teams(agent_list):
    # create an empty dictionary to hold agents with a given position
    print("Called find agents with shared positions and teams")
    positions_dict = {}
    
    # loop through the list of agents and group them by position
    for agent in agent_list:
        pos_key = tuple(agent.position)
        print(pos_key)
        if pos_key not in positions_dict:
            positions_dict[pos_key] = [agent]
        else:
            positions_dict[pos_key].append(agent)
    
    for k,v in positions_dict.items():
        if len(v)>=2 and len(set([agent.team_n for agent in v]))!=1:
            engagement(v)
        
initialize_referee()



    




