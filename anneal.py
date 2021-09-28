from graph import Graph
from greedy import Greedy
import matplotlib.pyplot as plt
import networkx as nx
import random
import math as math

# https://en.wikipedia.org/wiki/Simulated_annealing#Pseudocode

class Anneal():
    def __init__(self, graph):
        self.graph = graph
        self.T = 1.0e+10
        self.solution = []
        self.totalDistance = 0
        self.coolingFactor = 0.999
        self.stoppingTemp = 1e-8
        self.stoppingIter = 100000
        self.iter = 1


    def anneal(self):
        greedy = Greedy(self.graph)
        self.solution, self.totalDistance = greedy.run()
        firstDistance = self.totalDistance
        firstSolution = self.solution

        self.graph.drawGraph()
        while (self.iter < self.stoppingIter and self.T >= self.stoppingTemp):
            x = random.randint(0, len(self.graph.pos) - 1)
            y = random.randint(0, len(self.graph.pos) - 1)
            newSolution = self.solution.copy()
            newSolution[x], newSolution[y] = newSolution[y], newSolution[x] #Swap two random nodes
            print("New Solution {}".format(newSolution))

            newSolutionDist = self.totalDist(newSolution)
            print("Distance: {}".format(newSolutionDist))

            if (newSolutionDist < self.totalDistance):
                self.solution = newSolution
                self.totalDistance = newSolutionDist
                print("KEPT On immediate better value")
                print()
            else:
                print("Exponential probability value:")
                print(math.exp(-abs(newSolutionDist - self.totalDistance) / self.T))
                if (random.random() < math.exp(-abs(newSolutionDist - self.totalDistance) / self.T)): # Negative exponential as probability distribution
                    self.solution = newSolution
                    self.totalDistance = newSolutionDist
                    print("KEPT On random assignment")
                    print()
                    #self.drawAnneal()
                else:
                    print("NOT KEPT")
                    print()

            self.T *= self.coolingFactor
            self.iter += 1

        self.drawAnneal()
        print("First Distance: {}".format(firstDistance))
        print("First Solution: {}".format(firstSolution))
        print("Last Distance: {}".format(self.totalDistance))
        print("Last Solution: {}".format(self.solution))
        return (self.solution)

    def totalDist(self, solution):
        dist = 0
        for i in range(len(solution) - 1):
            dist += self.graph.getDistance(solution[i], solution[i + 1])
        dist += self.graph.getDistance(solution[len(solution) - 1], solution[0])
        return (dist)

    def getEdgesFrom(self, sol):
        res = []
        for i in range(len(sol) - 1):
            tuple = (sol[i], sol[i + 1])
            res.append(tuple)
        res.append((sol[len(sol) - 1], sol[0]))
        return (res)

    def drawAnneal(self):
        G = nx.Graph()
        G.add_nodes_from(g.pos)
        res = self.getEdgesFrom(self.solution)
        G.add_edges_from(res)
        nx.draw_networkx(G, g.pos)
        plt.show()

g = Graph(10)
g.addNodes()

anneal = Anneal(g)
anneal.anneal()
