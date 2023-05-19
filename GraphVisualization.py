import networkx as nx
import matplotlib.pyplot as plt
from vertex import vertex
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b,c):
        x = a.name
        y = b.name
        temp = [x, y, c]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.DiGraph()
        G.add_weighted_edges_from(self.visual)
        nx.draw_networkx(G)
        edge_labels = nx.get_edge_attributes(G, "weight")
        plt.show()

