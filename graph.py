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
        self.pos = {i:(random.randint(0,500), random.randint(0,500)) for i in self.V}

    def drawGraph(self):
        G = nx.Graph()
        G.add_nodes_from(self.pos)
        G.add_edges_from(self.E)
        nx.draw_networkx(G, self.pos)
        plt.show()

    def getDistance(self, a, b):
        #sqrt((A_x - B_x) + (A_y - B_y)^2)
        return (math.sqrt(pow((self.pos[a][0] - self.pos[b][0]), 2) + pow((self.pos[a][1] - self.pos[b][1]), 2)))

    def addEdge(self, a, b):
        self.E.append((a, b))

# Tests
#g = Graph(20)
#g.addNodes()
#g.drawGraph()
#g.addEdge(1,2)
#g.drawGraph()

#print(g.pos[1])
#print(g.pos[2])
#print(g.getDistance(1,2))
