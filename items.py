"""
Load libraries
"""

import pandas as pd

def get_item_df():
    """Generate a df of the items in bedwars and their cost

    Returns:
        item_df: df of items in bedwars
    """
    # item_str follows the form: name, cost, power, offense, defense
    item_str = """wool 4 iron .1 .1 .1
    clay 12 iron 0 0 .2
    wood 4 gold 0 0 .2
    glass 12 iron 0 0 .3
    endstone 24 iron 0 0 .3
    ladders 4 iron 0 0 .1
    obsidian 4 emeralds 0 0 .7
    stone_sword 10 iron .2 0 0 
    iron_sword  	7 gold .5 0 0
    diamond_sword 	4 emeralds .7 0 0
    knockback_stick 	5 gold .3 0 0
    chain_armor 	24 iron .2 0 0
    iron_armor 	12 gold .5 0 0
    diamond_armor 	6 emeralds .8 0 0 
    shears 20 iron 0 .2 0
    wooden_axe   10 iron 0 .3 0
    stone_axe   10 iron 0 .4 0
    iron_axe   3 gold 0 .5 0
    diamond_axe   6 gold 0 .6 0
    wooden_pickaxe  10 iron 0 .4 0
    iron_pickaxe   10 iron 0 .5 0
    gold_pickaxe  3 gold 0 .7 0
    diamond_pickaxe   6 gold 0 .9 0
    bow  	12 gold .5 0 0
    bow_power 	20 gold .7 0 0
    bow_punch 	6 emeralds .8 0 0
    arrows 	2 gold .2 0 0
    speed 	1 emerald .5 0 0
    jump	1 emerald .7 0 0
    invis	2 emeralds .3 .9 0
    gapple 	3 gold .7 0 0
    bed_bug	24 iron .1 0 0
    golem	120 iron .3 0 0
    fireball  	40 iron .8 0 0
    tnt 	4 gold .1 .8 0
    pearl 	4 emeralds .8 .5 0
    bucket 	2 gold 0 0 .4
    bridge 	1 emerald .3 .5 0
    milk 	4 gold 0 .8 0
    sponge  	2 gold 	0 .3 0
    tower 	24 iron .2 .3 .2 """

    item_lines = item_str.split('\n')
    item_names = [item_line.split()[0] for item_line in item_lines]
    item_costs = [{item_line.split()[2]:float(item_line.split()[1])} for item_line in item_lines]
    item_power = [float(item_line.split()[3]) for item_line in item_lines]
    item_offense = [float(item_line.split()[4]) for item_line in item_lines]
    item_defense = [float(item_line.split()[5]) for item_line in item_lines]

    item_df = pd.DataFrame({'item_names':item_names,'item_costs':item_costs,'item_power':item_power,'item_offense':item_offense,'item_defense':item_defense})

    return item_df
