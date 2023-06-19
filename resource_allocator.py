import generators  # imports the 'generators' module

import ticks  # imports the 'ticks' module

def resource_master(bases, diamonds, emeralds):  # defines a function called 'resource_master' that takes in three parameters: 'bases', 'diamonds', and 'emeralds'
    current_tick = get_ticks()  # assigns the value returned by the 'get_ticks()' function to the 'current_tick' variable
    allocate_iron(bases)  # calls the 'allocate_iron' function with the 'bases' parameter
    if current_tick % 2 = 0:  # checks if the remainder of 'current_tick' divided by 2 is equal to 0
        allocate_gold(bases)  # calls the 'allocate_gold' function with the 'bases' parameter
    if current_tick % 5 = 0:  # checks if the remainder of 'current_tick' divided by 5 is equal to 0
        allocate_diamonds(diamonds)  # calls the 'allocate_diamonds' function with the 'diamonds' parameter
    if current_tick % 10 = 0:  # checks if the remainder of 'current_tick' divided by 10 is equal to 0
        allocate_emeralds(emeralds)  # calls the 'allocate_emeralds' function with the 'emeralds' parameter

def allocate_iron(bases):  # defines a function called 'allocate_iron' that takes in one parameter: 'bases'
    for base in bases:  # loops through each 'base' in the 'bases' parameter
        generators.base.iron += 3  # adds 3 iron units to the 'iron' attribute of the 'base' object in the 'generators' module

def allocate_gold(bases):  # defines a function called 'allocate_gold' that takes in one parameter: 'bases'
    for base in bases:  # loops through each 'base' in the 'bases' parameter
        generators.base.gold += 1  # adds 1 gold unit to the 'gold' attribute of the 'base' object in the 'generators' module

def allocate_diamonds(diamonds):  # defines a function called 'allocate_diamonds' that takes in one parameter: 'diamonds'
    for diamond in diamonds:  # loops through each 'diamond' in the 'diamonds' parameter
        generators.diamond.diamonds +=1  # adds 1 diamond unit to the 'diamonds' attribute of the 'diamond' object in the 'generators' module

def allocate emeralds(emeralds):  # defines a function called 'allocate emeralds' that takes in one parameter: 'emeralds'
    for emerald in emeralds:  # loops through each 'emerald' in the 'emeralds' parameter
        generators.emerald.emeralds += 1  # adds 1 emerald unit to the 'emeralds' attribute of the 'emerald' object in the 'generators' module

