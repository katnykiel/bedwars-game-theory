import plotly.graph_objs as go
import numpy as np
import time
import os
from create_map import initialize_map
# from agent import *

# agent_list = get_test_agents()

def quick_plot(positions):
    # find the maximum x and y values to determine grid size
    n = len(positions)

    # create the empty grid of dots
    grid = [['.' for _ in range(n+1)] for _ in range(n+1)]

    # replace the dots with indices for each position
    for i, pos in enumerate(positions):
        x, y = pos
        grid[x][y] = str(i)
        
    # join the characters in each row with spaces, then join all rows with newlines
    block = '\n'.join([' '.join(row) for row in grid])
    return grid

def get_animation(positions):
    frames = [go.Frame(data = get_heatmap(quick_plot(position))) for position in positions]
    test_fig = go.Figure(get_heatmap(quick_plot(positions[0])))
    test_fig.show()

    fig = go.Figure(
    data=[get_heatmap(quick_plot(positions[0]))], 
    layout=go.Layout(
        title = "minecwaft",
        xaxis = {'showticklabels':False},
        yaxis = {'showticklabels':False},
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=100))])])]
        ), frames=frames )

    return fig 

def get_heatmap(position):
    print(position)
    # Create a new game map array where 0 values are replaced with NaN
    z = np.where(position == '.', np.nan, position)
    # Create the heatmap trace with custom colorscale
    heatmap = go.Heatmap(z=z)
    return heatmap

def get_plot(game_map, positions):

    # positions = [agent.position for agent in agent_list]
    
    # Define the colorscale for the heatmap
    colorscale = [[0, 'white'], [1, 'black']]

    # Create a new game map array where 0 values are replaced with NaN
    z = np.where(game_map == 0, np.nan, game_map)

    # Create the heatmap trace with custom colorscale
    heatmap = go.Heatmap(z=z, colorscale=colorscale)

    # Set the layout for the plot
    layout = go.Layout(title='Game Map Heatmap')

    # Create the figure object
    fig = go.Figure(data=[heatmap], layout=layout)

    for i in range(len(positions)):
        x, y = positions[i]
        fig.add_annotation(x=x, y=y, text=f"Agent {i+1}", showarrow=False)
    
        fig.update_layout(annotations=fig.layout.annotations)
    
    return fig



# Generate a plotly image from an array of spins -1 and 1
def get_ising_plot(spin):
    img = np.array(spin, dtype = object)
    for i in range(len(spin[0])):
        for j in range(len(spin[1])):
            if spin[i,j] == 1:
                img[i,j] = [255,255,255]
            else:
                img[i,j] = [0,0,0]
    image = go.Image(z=img)
    return image

# Stich together plotly frames to create an animation 
def get_ising_video(frames, initial_spin):
    fig = go.Figure(
    data=[get_ising_plot(initial_spin)], 
    layout=go.Layout(
        title = "Ising model demonstration",
        xaxis = {'showticklabels':False},
        yaxis = {'showticklabels':False},
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=1))])])]
        ), frames=frames )

    return fig 

