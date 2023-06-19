import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from sprites import get_agent_sprites,get_base_sprite,get_diamond_sprite,get_emerald_sprite
import referee

def get_map_trace(pixel_array):
    """returns a trace given a set of pixelss

    Args:
        pixel_array (array): array of rgb colors

    Returns:
        trace: a plotly image trace of the pixels
    """    
    
    trace = go.Image(z=pixel_array)
    return trace

def get_animation(traces):
    return None

def get_figure(agents):
    # test the bed making sprites
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
        
    # add agents as additional opaque trace
    agent_pixel_array = get_agent_sprites(agents)
    agent_trace = go.Image(z=agent_pixel_array,opacity=.5)

    trace = get_map_trace(pixels)
    fig = go.Figure()
    fig.add_trace(trace)  
    fig.add_trace(agent_trace)  
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.show()

def quick_plot(positions):
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

def get_animation_old(positions):
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

def get_plot(game_map):

    positions = referee.get_agent_postions()
    
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

