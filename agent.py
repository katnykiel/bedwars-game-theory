"""
Load items df
"""

from items import get_item_df
class Agent:
    """Define an 'agent' in bedwars that acts upon a grid
    """
    def __init__(self,team_n,personality = {},skills = {}):
        self.personality = personality
                       #     {'aggressiveness':0, 'teamwork':0,
                       #     'emerald_desire':0,'diamond_desire':0} # traits prone to mutation
        self.skills = skills #{'PvP':0,'speed':0} # traits NOT prone to mutation
        self.items = {} # what items does the agent possess?
        self.wealth = {'iron':0,'gold':0,'diamond':0,'emerald':0}
        # what weath does the agent possess?
        self.team_n=team_n
        self.position = self.get_starting_position # the x,y location of the agent

    def get_traits(self):
        """Calculate the 'traits' of the agent that will be used in decision-making

        Returns:
            traits: set of traits to determine decision making

        things to keep in mind
        some items raise bed_breaking 
        (do we just keep a bed_defending stat? add them to some base point?)
        """

        traits = {'power':0,'bed_offense':0,'bed_defense':0} | self.personality
        return traits

    def get_starting_position(self):
        """Return starting x,y coordinates of some Agent given team n

        Returns:
            starting_pos: x,y coord of bed
        """
        bed_map = {0:[0,2],1:[0,4],2:[2,6],3:[4,6],
                   4:[6,4],5:[2,6],6:[4,0],7:[2,0]}
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


    def make_decision(self):
        """ things to keep in mind
        what are the options?
        - buy item 
        - move to target
        - defend

        include the wealth and position
        more wealth, less aggressive
        """

        decision = []

        return decision

def get_test_agents():
    """test by returning a list of agents

    Returns:
       agent_list: list of Agent objects
    """    
    agent_list = []
    for i in range(8):
        agent_list.append(Agent(i))
    return agent_list

def main():
    """testing loop for agents!
    """
    item_df = get_item_df()
    print(item_df)

main()
