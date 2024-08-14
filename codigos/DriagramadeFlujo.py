# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', font_weight='bold')
plt.show()
