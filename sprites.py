# define sprite objects as sets of pixels with colors to be plotted

import plotly.express as px
import plotly.graph_objects as go

def get_team_color(team_n):
    """Get team color to plot

    Args:
        team_n (int): team number

    Returns:
        color: team color 
    """    
    colors = px.colors.qualitative.Plotly
    hex_code = colors[team_n][1:]
    red, green, blue = int(hex_code[:2], 16), int(hex_code[2:4], 16), int(hex_code[4:], 16)
    return [red,green,blue]

def get_base_sprite(pos, team_n):
    """get sprite for bedwars base to plot in gui

    Args:
        pos (list): [x,y] position of base in 7x7 grid
        team_n (int): team number

    Returns:
        pixel_array (array): 49x49 array of colors
    """

    # define pixel set
    pixel_array = [[[255,255,255] for x in range(49)] for y in range(49)]

    # shift the centers to new positions
    new_pos = [7*coord+3 for coord in pos]

    # get some base of size 3
    base_size = 3
    base_blocks = list(range(-base_size,base_size+1))
    for i in base_blocks:
        for j in base_blocks:           
            pixel_array[new_pos[0]+i][new_pos[1]+j] = [150,150,150]

    pixel_array[new_pos[0]][new_pos[1]] = [255,255,254]

    # add bed pillow
    if pos[0]==0:
        pixel_array[new_pos[0]+1][new_pos[1]] =get_team_color(team_n)
    if pos[0]==6:
        pixel_array[new_pos[0]-1][new_pos[1]] = get_team_color(team_n)
    if pos[1]==0:
        pixel_array[new_pos[0]][new_pos[1]+1] = get_team_color(team_n)
    if pos[1]==6:
        pixel_array[new_pos[0]][new_pos[1]-1] = get_team_color(team_n)

    return pixel_array

def get_emerald_sprite(pos):
    """get sprite for emerald gen to plot in gui

    Args:
        pos (list): [x,y] position of base in 7x7 grid

    Returns:
        pixel_array (array): 49x49 array of colors
    """

    # define pixel set
    pixel_array = [[[255,255,255] for x in range(49)] for y in range(49)]

    # shift the centers to new positions
    new_pos = [7*coord+3 for coord in pos]

    # get some base of size 3
    base_size = 3
    base_blocks = list(range(-base_size,base_size+1))
    for i in base_blocks:
        for j in base_blocks:           
            pixel_array[new_pos[0]+i][new_pos[1]+j] = [200,200,200]

    base_size = 1
    base_blocks = list(range(-base_size,base_size+1))
    for i in base_blocks:
        for j in base_blocks:           
            pixel_array[new_pos[0]+i][new_pos[1]+j] = [180,180,180]

    pixel_array[new_pos[0]][new_pos[1]] = [60,230,120]

    return pixel_array


def get_diamond_sprite(pos):
    """get sprite for diamond gen to plot in gui

    Args:
        pos (list): [x,y] position of base in 7x7 grid

    Returns:
        pixel_array (array): 49x49 array of colors
    """

    # define pixel set
    pixel_array = [[[255,255,255] for x in range(49)] for y in range(49)]

    # shift the centers to new positions
    new_pos = [7*coord+3 for coord in pos]

    # get some base of size 3
    base_size = 3
    base_blocks = list(range(-base_size,base_size+1))
    for i in base_blocks:
        for j in base_blocks:           
            pixel_array[new_pos[0]+i][new_pos[1]+j] = [200,200,200]

    base_size = 1
    base_blocks = list(range(-base_size,base_size+1))
    for i in base_blocks:
        for j in base_blocks:           
            pixel_array[new_pos[0]+i][new_pos[1]+j] = [180,180,180]

    pixel_array[new_pos[0]][new_pos[1]] = [90,230,210]

    return pixel_array

def get_agent_ordering(pos):
    """define the orientation with which any new agents are placed on a 49x49 grid

    Args:
        pos (list): [x,y] of agent on 7x7 grid                  

    Returns:
        list: offset list for a given site
    """

    if pos[0]==0 and (pos[1] in [2,4]):
        offset = [[0,2],[-2,0],[0,-2],[2,0]]
    elif pos[0]==6 and (pos[1] in [2,4]):
        offset = [[0,-2],[2,0],[0,2],[-2,0]]
    elif pos[1]==0 and (pos[0] in [2,4]):
        offset = [[-2,0],[0,-2],[2,0],[0,2]]
    elif pos[1]==6 and (pos[0] in [2,4]):
        offset = [[2,0],[0,2],[-2,0],[0,-2]]
        # offset = [[2,0],[0,2],[-2,0],[0-2]]

    else:
        offset = [[-2,0],[0,-2],[2,0],[0,2]]
    offset.append([-2,-2])
    offset.append([-2,2])
    offset.append([2,2])
    offset.append([2,-2])
    offset.append([-1,-2])
    offset.append([1,-2])
    offset.append([2,-1])
    offset.append([2,1])
    offset.append([1,2])
    offset.append([-1,2])
    offset.append([-2,1])
    offset.append([-2,-1])

    return offset

def get_agent_sprites(agents):

    # loop through the list of agents and group them by position
    positions_dict = {}
    for agent in agents:
        pos_key = tuple(agent.position)
        if pos_key not in positions_dict:
            positions_dict[pos_key] = [agent]
        else:
            positions_dict[pos_key].append(agent)
    
    # define pixel set
    pixel_array = [[[255,255,255] for x in range(49)] for y in range(49)]

    for position, agents in positions_dict.items():
        offset = get_agent_ordering(position)
        new_pos = [7*coord+3 for coord in position]
        for i,agent in enumerate(agents):
            if len(agents)==1:
                pixel_array[new_pos[0]][new_pos[1]] = get_team_color(agent.team_n)
            else:
                pixel_array[new_pos[0]+offset[i][0]][new_pos[1]+offset[i][1]] = get_team_color(agent.team_n)

    return pixel_array
