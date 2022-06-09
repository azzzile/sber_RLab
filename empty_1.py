import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from grave import plot_network
from grave.style import use_attributes

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def hilighter(event):
    print(event.edges)
    # if we did not hit a node, bail
    if not hasattr(event, 'nodes') or not event.nodes:
        return

    # pull out the graph,
    graph = event.artist.graph

    # clear any non-default color on nodes
    for node, attributes in graph.nodes.data():
        attributes.pop('color', None)

    for u, v, attributes in graph.edges.data():
        attributes.pop('width', None)

    for node in event.nodes:
        graph.nodes[node]['color'] = 'C1'

        for edge_attribute in graph[node].values():
            edge_attribute['width'] = 3

    # update the screen
    event.artist.stale = True
    event.artist.figure.canvas.draw_idle()


mpl.use('Qt5Agg')
graph = nx.barbell_graph(10, 14)

fig, ax = plt.subplots()
art = plot_network(graph, ax=ax, node_style=use_attributes(),
                   edge_style=use_attributes())

art.set_picker(10)
ax.set_title('Click on the nodes!')
fig.canvas.mpl_connect('pick_event', hilighter)
plt.show()

