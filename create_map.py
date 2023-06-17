import numpy as np

'''
This code governs the rules of the game.
'''

def initialize_map():
    '''
    This function initializes a map, it takes no arguments. 
    Returns the map as a numpy array of dimensions 7 by 7
    Each element of the array can have values of 0, 1, 2, 3, 4
    0 = Air
    1 = Base
    2 = Diamond
    3 = Emerald
    4 = Bridge
    '''
    
    map = np.zeros((7, 7)) # Initialize a numpy array of dimensions 7 x 7
    print("Map initialized.") # Log

    map = np.array([[2,0,1,0,1,0,2], # Define initial conditions of the map
                    [0,0,0,0,0,0,0],
                    [1,0,3,0,3,0,1],
                    [0,0,0,0,0,0,0],
                    [1,0,3,0,3,0,1],
                    [0,0,0,0,0,0,0],
                    [2,0,1,0,1,0,2]])
    print(map) # Print map

    return map

initialize_map()

