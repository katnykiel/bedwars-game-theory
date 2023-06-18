import plotly.graph_objs as go
import numpy as np
from agent import *

agent_list = get_test_agents()

def get_plot(game_map):

    positions = get_agent_postions()
    
    # Define the colorscale for the heatmap
    colorscale = [[0, 'white'], [1, 'black']]

    # Create a new game map array where 0 values are replaced with NaN
    z = np.where(game_map == 0, np.nan, game_map)

    # Create the heatmap trace with custom colorscale
    heatmap = go.Heatmap(z=z, colorscale=colorscale)

    # Set the layout for the plot
    #layout = go.Layout(title='Game Map Heatmap')

    # Create the figure object
    #fig = go.Figure(data=[heatmap], layout=layout)

    #for i in range(len(positions)):
        #x, y = positions[i]
        #fig.add_annotation(x=x, y=y, text=f"Agent {i+1}", showarrow=False)
    
        #fig.update_layout(annotations=fig.layout.annotations)
    return heatmap

def get_agent_postions():
    """
    Get agent positions

    Calls the get_test_agents function to return a list of agents
    initializes agent_positions list
    iterates over agents list to append the position of each agent to the agent position
    return agent position list

    """
    
    agents = get_test_agents() # get test agents
    agent_positions = [agent.position for agent in agents]

    return agent_positions # return the list



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
def get_agent_video(frames, initial_map):
    fig = go.Figure(
    data=[get_plot(initial_map)], 
    layout=go.Layout(
        title = "Minecwaft",
        xaxis = {'showticklabels':False},
        yaxis = {'showticklabels':False},
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=1_000))])])]
        ), frames=frames )

    return fig 

