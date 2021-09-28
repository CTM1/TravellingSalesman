import matplotlib.pyplot as plt
import networkx as nx
import random
import math as math

class Graph():
    def __init__(self, nodes):
        # creates nice even graph
        # self.graph = nx.erdos_renyi_graph(nodes, 1)
        self.numberOfNodes = nodes
        self.V = range(nodes)
        self.E = []
        self.pos = []

    def addNodes(self):
        self.pos = {i:(random.randint(0,2000), random.randint(0,2000)) for i in self.V}

    def drawGraph(self):
        G = nx.Graph()
        G.add_nodes_from(self.pos)
        G.add_edges_from(self.E)
        nx.draw_networkx(G, self.pos)
        plt.show()

    def getDistance(self, a, b):
        return (math.sqrt(pow((self.pos[a][0] - self.pos[b][0]), 2) + pow((self.pos[a][1] - self.pos[b][1]), 2)))

    def addEdge(self, a, b):
        self.E.append((a, b))
