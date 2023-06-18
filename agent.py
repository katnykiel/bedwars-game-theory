"""
Load items df
"""
import random
from items import get_item_df
from gui import *

class Agent:
    """Define an 'agent' in bedwars that acts upon a grid
    """
    def __init__(self,team_n,personality = {},skills = {}):
        self.personality = personality
                       #     {'aggressiveness':0, 'teamwork':0,
                       #     'emerald_desire':0,'diamond_desire':0} # traits prone to mutation
        self.skills = skills #{'PvP':0,'speed':0} # traits NOT prone to mutation
        self.items = [] # what items does the agent possess?
        self.wealth = {'iron':0,'gold':0,'diamond':0,'emerald':0}
        # what weath does the agent possess?
        self.team_n=team_n
        self.position = self.get_starting_position() # the x,y location of the agent
        self.traits = self.get_traits()
        self.path = [] # current path the agent is on
        self.bed = True # if bed is alive
        self.alive = True

    def get_traits(self):
        """Calculate the 'traits' of the agent that will be used in decision-making

        Returns:
            traits: set of traits to determine decision making

        """

        agent_item_df = item_df[item_df['item_names'].isin(self.items)]
        power = agent_item_df['item_power'].sum()
        offense = agent_item_df['item_offense'].sum()
        defense = agent_item_df['item_defense'].sum()

        traits = {'power':power,'offense':offense,'defense':defense} | self.personality
        self.traits = traits
        return traits

    def get_starting_position(self):
        """Return starting x,y coordinates of some Agent given team n

        Returns:
            starting_pos: x,y coord of bed
        """
        bed_map = {0:[0,2],1:[0,4],2:[2,6],3:[4,6],
                   4:[6,4],5:[6,2],6:[4,0],7:[2,0]}
        return bed_map[self.team_n]

    def die(self):
        """Reset attributes when an Agent dies
        """
        # reset position
        self.position = self.get_starting_position()
        # reset wealth
        self.wealth = 0
        # reset items
        items_to_keep = ['wool','clay','wood','glass','endstone','water',
                         'obsidian','ladders','chain_armor','iron_armor',
                         'diamond_armor','shears','wooden_axe','wooden_pickaxe']
        self.items = {k: v for k, v in self.items.items() if k in items_to_keep}
        self.path = []
        if not self.bed:
            self.alive = False
            self.position = [-1,-1]

    def make_decision(self):
        """ things to keep in mind
        what are the options?
        - buy item 
        - move to target
        - defend

        include the wealth and position
        more wealth, less aggressive
        """

        # for now, define some random variable as a target block
        target = [random.randint(0,6),random.randint(0,6)]
        path = self.get_path(target) 
        self.path = path
    
    def move(self):
        if len(self.path) == 0:
            self.make_decision()
        self.position = self.path[0]
        self.path.pop(0)

    def get_path(self, target):
        start_pos = self.position
        end_pos = target
        
        if start_pos == end_pos:
            return [start_pos]

        diff_x = end_pos[0] - start_pos[0]
        diff_y = end_pos[1] - start_pos[1]

        path = []
        
        # Move horizontally
        if diff_x > 0:
            for i in range(1, diff_x + 1):
                path.append((start_pos[0] + i, start_pos[1]))
        else:
            for i in range(-1, diff_x - 1, -1):
                path.append((start_pos[0] + i, start_pos[1]))
        
        # Move vertically
        if diff_y > 0:
            for i in range(1, diff_y + 1):
                path.append((end_pos[0], start_pos[1] + i))
        else:
            for i in range(-1, diff_y - 1, -1):
                path.append((end_pos[0], start_pos[1] + i))
        
        path.append(end_pos)
        return path

def get_test_agents():
    """test by returning a list of agents

    Returns:
       agent_list: list of Agent objects
    """    

    agent_list = []
    for i in range(16):
        agent_list.append(Agent(i%8,personality={'aggressiveness':random.random(), 'teamwork':random.random(),'emerald_desire':random.random(),'diamond_desire':random.random()}))
        
    for agent in agent_list:
        agent.items = item_df['item_names'].sample(n=5,replace=False)
        agent.get_traits();
    return agent_list

def run_test_game():
    """run a sample game for testing purposes
    """    
    agent_list = get_test_agents()
    [agent.make_decision() for agent in agent_list]
    # positions = []
    frames = []
    frames.append(get_frame(agent_list))
    for i in range (20):
        [agent.move() for agent in agent_list]
        # print(quick_plot([agent.position for agent in agent_list]),'\n')
        # positions.append([agent.position for agent in agent_list])
        frames.append(get_frame(agent_list))
    fig = get_animation(frames)
    # fig = get_animation_old(positions)
    fig.show()
   
    # get_animation(positions).show()

def main():
    """testing loop for agents!
    """
    # print(get_test_agents())
item_df = get_item_df()
main()

run_test_game()