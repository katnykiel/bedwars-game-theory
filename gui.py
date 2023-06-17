import plotly.graph_objs as go
import numpy as np
from agent import *

agent_list = get_test_agents()

def get_plot(game_map):
    

    positions = [agent.position for agent in agent_list]
    
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





