init_game_map = create_map.initialize_map()
game_map = init_game_map
fig = get_agent_video([go.Frame(data = get_plot(game_map))], init_game_map)

fig.show()

agent_list = get_test_agents()