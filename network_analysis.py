import networkx as nx
import matplotlib.pyplot as plt

def power_network():
    network = nx.DiGraph()
    # Add generators with cost functions ($/MWh)
    network.add_node("GenA", type="generator", cost=20)
    network.add_node("GenB", type="generator", cost=30)
    # Add loads (demand centers)
    network.add_node("Load1", type="load", demand=50)
    network.add_node("Load2", type="load", demand=30)
    # Add transmission lines with capacities
    network.add_edge("GenA", "Load1", capacity=60, resistance=0.1)
    network.add_edge("GenB", "Load1", capacity=40, resistance=0.15)
    network.add_edge("GenB", "Load2", capacity=50, resistance=0.2)

    return network

# Run and visualize network
grid = power_network()
print("Power Grid Created:", grid.nodes(data=True))
pos = nx.spring_layout(grid)
labels = {node: node for node in grid.nodes()}
nx.draw(grid, pos, with_labels=True, node_size=2000, node_color="lightblue")
nx.draw_networkx_labels(grid, pos, labels, font_size=10)
plt.title("Power Grid Network")
plt.show()