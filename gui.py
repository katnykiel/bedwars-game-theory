import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from sprites import get_agent_sprites,get_base_sprite,get_diamond_sprite,get_emerald_sprite

def get_map_trace(pixel_array):
    """returns a trace given a set of pixelss

    Args:
        pixel_array (array): array of rgb colors

    Returns:
        trace: a plotly image trace of the pixels
    """    
    
    trace = go.Image(z=pixel_array)
    return trace

def get_inital_map_pixels():
    """get the intial 49x49 map array

    Returns:
        pixels: 49x49 array of color codes
    """    
    bed_map = {0:[0,2],1:[0,4],2:[2,6],3:[4,6],
                    4:[6,4],5:[6,2],6:[4,0],7:[2,0]}

    emerald_map = {0:[2,2],1:[2,4],2:[4,2],3:[4,4]}

    diamond_map = {0:[0,0],1:[6,0],2:[0,6],3:[6,6]}

    # build sprites
    pixel_arrays = []
    for team_n in bed_map:
        pixel_arrays.append(get_base_sprite(bed_map[team_n],team_n))
    for gen in emerald_map:
        pixel_arrays.append(get_emerald_sprite(emerald_map[gen]))
    for gen in diamond_map:
        pixel_arrays.append(get_diamond_sprite(diamond_map[gen]))

    # combine pixels
    pixels = [[[255,255,255] for x in range(49)] for y in range(49)]
    for pixel_array in pixel_arrays:
        for i,sublist in enumerate(pixel_array):
            for j,color in enumerate(sublist):
                if color != [255,255,255]:
                    pixels[i][j]=color

    return pixels

def get_animation(frames):
    """get an animation of the agents moving around

    Args:
        frames (list[Frame]): list of Frame objects of map

    Returns:
        fig: animated go.Figure()
    """    
    fig = go.Figure(
    data=[get_map_trace(get_inital_map_pixels())], 
    layout=go.Layout(
        title = "minecwaft",
        xaxis = {'showticklabels':False},
        yaxis = {'showticklabels':False},
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=500))])])]
        ), frames=frames)
    return fig 

def get_frame(agents):
    """return a Frame object for the animation

    Args:
        agents (list(Agent)): list of Agent objects

    Returns:
        frame: go.Frame object
    """    
    map_pixel_array = get_inital_map_pixels()
    # add agents as additional opaque trace
    agent_pixel_array = get_agent_sprites(agents)
    # add agent pixels on top of map pixels
    pixels = map_pixel_array
    for i,sublist in enumerate(agent_pixel_array):
        for j,color in enumerate(sublist):
            if color != [255,255,255]:
                pixels[i][j]=color

    # agent_trace = go.Image(z=agent_pixel_array,opacity=.5)
    trace = get_map_trace(pixels)
    frame = go.Frame(data=[trace])
    # fig.update_xaxes(showticklabels=False)
    # fig.update_yaxes(showticklabels=False)
    # fig.show()
    return frame

def quick_plot(positions):
    """quick and dirty way to plot map in terminal, don't use this

    Args:
        positions (list of list of lists): coords :)

    Returns:
        grid (array): coords! i told you, don't use this 
    """    
    # find the maximum x and y values to determine grid size
    n = 7

    # create the empty grid of dots
    grid = [['.' for _ in range(n+1)] for _ in range(n+1)]

    # replace the dots with indices for each position
    for i, pos in enumerate(positions):
        x, y = pos
        grid[x][y] = str(i)
        
    # join the characters in each row with spaces, then join all rows with newlines
    block = '\n'.join([' '.join(row) for row in grid])
    return grid