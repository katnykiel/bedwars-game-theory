"""

This .py file will govern the time behavior of the game.

initialize_ticks()
get_ticks()
DO AGENT_ACTIONS
increment_ticks()

"""

def initialize_ticks():
    """
PURPOSE: initialize_ticks initializes a variable tick_counter to 0

RETURNS: tick_counter
    """
    
    tick_counter = 0 # initalizes the tick counter for the game referee

    return tick_counter

def increment_ticks(tick_counter):
    """Incrememt tick

    Args:
        tick_counter (integer): integer returned by the initialize ticks or get_ticks function. This will cause a recursive loop
        that will continue until one team is left standing

    Returns:
        tick_counter: tick_counter
    """
    tick_counter = tick_counter + 1

    return tick_counter

def get_ticks(tick_counter):
    """get ticks

    Args:
        tick_counter (integer): integer returned from increment_ticks function

    Returns:
        current_tick: the current tick of the game
    """

    current_tick = increment_ticks(tick_counter)
    return current_tick