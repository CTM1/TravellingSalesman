from graph import Graph
import random

class Greedy():
    def __init__(self, graph):
        self.graph = graph
        self.unvisited = [i for i in graph.V]
        self.totalDistance = 0
        self.solution = []

    def run(self, drawEndGraph=False, drawTurnGraph=False):
        self.totalDistance = 0
        currNode = self.unvisited[0]
        self.solution = [currNode]
        self.unvisited.remove(currNode)

        while (self.unvisited):
            nextNode = min(self.unvisited, key=lambda x: self.graph.getDistance(currNode, x)) # min(iterable, *iterables, key, default)
            self.unvisited.remove(nextNode)
            self.solution.append(nextNode)
            self.graph.addEdge(currNode, nextNode)
            self.totalDistance += self.graph.getDistance(currNode, nextNode)
            currNode = nextNode
            if (drawTurnGraph):
                self.graph.drawGraph()

        self.graph.addEdge(nextNode, self.solution[0])
        self.totalDistance += self.graph.getDistance(nextNode, self.solution[0])
        if (drawEndGraph):
            self.graph.drawGraph()

        return (self.solution, self.totalDistance)
