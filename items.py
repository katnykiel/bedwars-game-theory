"""
Load libraries
"""

import pandas as pd

def get_item_df():
    """Generate a df of the items in bedwars and their cost

    Returns:
        item_df: df of items in bedwars
    """
    # item_str follows the form: name, cost, power_stat, 
    item_str = """wool 4 iron
    clay 12 iron
    wood 4 gold
    glass 12 iron
    endstone 24 iron
    ladders 4 iron
    obsidian 4 emeralds
    stone_sword 10 iron
    iron_sword  	7 gold
    diamond_sword 	4 emeralds 
    knockback_stick 	5 gold
    chain_armor 	24 iron
    iron_armor 	12 gold
    diamond_armor 	6 emeralds
    shears 20 iron
    wooden_axe   10 iron
    stone_axe   10 iron
    iron_axe   3 gold
    diamond_axe   6 gold 
    wooden_pickaxe  10 iron
    iron_pickaxe   10 iron
    gold_pickaxe  3 gold
    diamond_pickaxe   6 gold
    bow  	12 gold
    bow_power 	20 gold
    bow_punch 	6 emeralds
    arrows 	2 gold
    speed 	1 emerald
    jump	1 emerald
    invis	2 emeralds
    gapple 	3 gold
    bed_bug	24 iron
    golem	120 iron
    fireball  	40 iron
    tnt 	4 gold 
    pearl 	4 emeralds
    bucket 	2 gold 	
    bridge 	1 emerald
    milk 	4 gold
    sponge  	2 gold 	
    tower 	24 iron """

    item_lines = item_str.split('\n')
    print(item_lines)
    item_names = [item_line.split()[0] for item_line in item_lines]
    item_costs = [{item_line.split()[-1]:item_line.split()[-2]} for item_line in item_lines]

    item_df = pd.DataFrame({'item_names':item_names,'item_costs':item_costs})
    return item_df

