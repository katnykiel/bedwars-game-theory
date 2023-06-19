import referee
import create_map
import gui
import agent

def main():
    """ Main gameplay loop
    Init map
    Init GUI
    Init referee

    get positions
    check for engagements
    check for resources
    check for bed attack
    check for bed destroy
    eliminate players
    check number of alive players
    repeat
    """

    players_alive = sum([1 for agent in agent_list if agent.alive])

    referee.initialize_referee()
    create_map.initialize_map()

    while players_alive > 1:
    
        agent_list = agent.get_test_agents()
        agent_positions = referee.get_agent_positions()

        referee.find_agents_with_shared_positions_and_teams(agent_list)

        referee.allocate_resources(agent_positions)