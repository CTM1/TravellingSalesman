from graph import Graph
from greedy import Greedy

print("Creating node graph")
g = Graph(10)
g.addNodes()
g.drawGraph()

print("Solving node graph with greedy method")
greedy = Greedy(g)
greedy.run(drawTurnGraph=True, drawEndGraph=True)
