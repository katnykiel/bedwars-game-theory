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

    players_alive = 8

    initialize_referee()
    initialize_map()

    while players_alive > 1:
    
        agent_list = get_test_agents()
        agent_positions = get_agent_positions()

        find_agents_with_shared_positions_and_teams(agent_list)

        allocate_resources(agent_positions)
        