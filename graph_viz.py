import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.collections import PathCollection
import networkx as nx
import yaml
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def draw_graph(cur_floor, cur_config_path, cur_graph_path):
    if __name__ == "__main__":
        def onpick(event):
            if isinstance(event.artist, PathCollection):
                all_nodes = event.artist
                ind = event.ind[0]  # event.ind is a single element array.
                nodes = list(pos.keys())
                this_node_name = nodes[ind]

                # Set the colours for all the nodes, highlighting the picked node with
                # a different colour:

                COLOR_MAP[ind]=COLORS['picked'][this_node_name.split("_")[1]]
                if PREV_IND is not None:
                    COLOR_MAP[PREV_IND] = COLORS[nodes[PREV_IND].split("_")[1]]

                all_nodes.set_facecolors(COLOR_MAP)
                # Update the plot to show the change:
                fig.canvas.draw()
                #PREV_IND = ind


        with open(cur_config_path) as f:
            storage = yaml.safe_load(f)

        PREV_IND = None
        COLORS = {"normal": {"L": "#55efc4", "CS": "#ffeaa7", "A": "#74b9ff", "R": "#adef52", "E": "#ef8c69"},
                  "picked": {"L": "#52D6AB", "CS": "#D7C38A", "A": "#6299D6", "R": "#8FCC54", "E": "#D57368"}}

        mpl.use('Qt5Agg')

        G = nx.read_graphml(cur_graph_path)

        modules = storage["modules"]

        pos = {}
        nodes = G.nodes()

        base_gap_x = 20
        base_gap_y = 30
        scale = 10

        COLOR_MAP = []
        cur_nodes = []
        #cur_floor_G = nx.Graph()

        for node in nodes:
            module_id, typo, floor, rack, cell = map(lambda i: int(i) if i.isdigit() else i, node.split("_"))
            if floor == cur_floor or typo == "L":
                cur_nodes.append(node)

        cur_floor_G = G.subgraph(cur_nodes)
        cur_floor_G = cur_floor_G.to_undirected()

        for node in cur_floor_G.nodes():
            module_id, typo, floor, rack, cell = map(lambda i: int(i) if i.isdigit() else i, node.split("_"))
            if typo == "L":
                pos[node] = [
                    # x
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    # y
                    -base_gap_y * scale * modules[module_id - 1]["lift"]["weight"]
                ]

            elif typo == "CS":
                pos[node] = [
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    10
                ]

            elif typo == "A":
                pos[node] = [
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    base_gap_y * scale * cell
                ]
            elif typo == "R":
                pos[node] = [
                    # x
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    # y
                    -base_gap_y * scale * modules[module_id - 1]["lift"]["weight"]
                ]

            elif typo == "E":
                pos[node] = [
                    # x
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    # y
                    -base_gap_y * scale * modules[module_id - 1]["lift"]["weight"]
                ]
            COLOR_MAP.append(COLORS["normal"][typo])



        #draw graph
        plt.gca().set_axis_off()
        nodes = nx.draw_networkx_nodes(cur_floor_G, pos, node_color=COLOR_MAP, label=1, node_size=200)

        nodes.set_picker(5)

        nx.draw_networkx_labels(cur_floor_G, pos, font_size=5)
        nx.draw_networkx_edges(cur_floor_G, pos, width=1)
        nx.draw_networkx_edge_labels(cur_floor_G, pos, edge_labels=nx.get_edge_attributes(cur_floor_G, 'weight'), font_size=5)

        fig = plt.gcf()

        # Bind our onpick() function to pick events:
        fig.canvas.mpl_connect('pick_event', onpick)

        plt.show()
