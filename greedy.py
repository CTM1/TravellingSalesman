from graph import Graph

class Greedy():
    def __init__(self, graph):
        self.graph = graph
        self.notVisited = graph.pos.copy()
        self.totalDistance = 0

    def run(self):
        for i in range(0, self.graph.numberOfNodes):
            min = self.graph.getDistance(i, i + 1)
            visitedNode = i + 1

            for node in self.notVisited:
                dist = self.graph.getDistance(1, node)
                if (dist < min):
                    min = dist
                    visitedNode = node

            self.notVisited.pop(visitedNode)
            self.graph.addEdge(i, visitedNode)
            self.totalDistance += min
            self.graph.drawGraph()

            print("graph.pos:")
            print(self.graph.pos)
            print("graph.E:")
            print(self.graph.E)
            print("notVisited:")
            print(self.notVisited)
            print("i:")
            print(i)




    def printState(self):
        print("graph.pos:")
        print(self.graph.pos)


g = Graph(5)
g.addNodes()

greedy = Greedy(g)
greedy.run()

# Testing for pos copy
#greedy.notVisited.pop(1)
#print(greedy.notVisited)
#print(g.pos)
