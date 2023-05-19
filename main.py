from vertex import vertex
from Graph import Graph
from GraphVisualization import GraphVisualization

z = vertex(0)
o = vertex(1)
t = vertex(2)
th = vertex(3)
f = vertex(4)
fi = vertex(5)
six = vertex(6)
seven = vertex(7)
eight = vertex(8)
G = GraphVisualization()
G.addEdge(z, o,4)
G.addEdge(z, seven,8)
G.addEdge(o, t,8)
G.addEdge(o, seven,11)
G.addEdge(t, th,7)
G.addEdge(t, eight,2)
G.addEdge(t, fi,4)
G.addEdge(th, f,9)
G.addEdge(th, fi,14)
G.addEdge(f, fi,10)
G.addEdge(fi, six,2)
G.addEdge(six, seven,1)
G.addEdge(six, eight,6)
G.addEdge(seven, eight,7)
G.visualize()
vertices = {z,o,t,th,f,fi,six}
edges = {(z,o):2,(z,th):8,(o,th):4,(o,f):1,(o,t):10,(o,fi):2,(t,fi):5,(th,f):5,(th,six):1,(f,six):4,(f,fi):2,(fi,six):7}
g = Graph(vertices,edges)
g.prim(z)
g.Dijkstra(z)
""""
v = {z,o,t,th,f,fi,six,seven,eight}
e ={(z,o):4,(z,seven):8,(o,t):8,(o,seven):11,(t,th):7,(t,eight):2,(t,fi):4,(th,f):9,(th,fi):14,(f,fi):10,(fi,six):2,(six,seven):1,(six,eight):6,(seven,eight):7}
g = Graph(v,e)
g.prim(z)
g.Dijkstra(z)
"""
