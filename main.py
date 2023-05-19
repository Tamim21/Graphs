from vertex import vertex
from Graph import Graph
z = vertex(0)
o = vertex(1)
t = vertex(2)
th = vertex(3)
f = vertex(4)
fi = vertex(5)
six = vertex(6)
seven = vertex(7)
eight = vertex(8)
vertices = {z,o,t,th,f,fi,six}
edges = {(z,o):2,(z,th):8,(o,th):4,(o,f):1,(o,t):10,(o,fi):2,(t,fi):5,(th,f):5,(th,six):1,(f,six):4,(f,fi):2,(fi,six):7}
g = Graph(vertices,edges)
g.prim(z)
g.Dijkstra(z)



v = {z,o,t,th,f,fi,six,seven,eight}
e ={(z,o):4,(z,seven):8,(o,t):8,(o,seven):11,(t,th):7,(t,eight):2,(t,fi):4,(th,f):9,(th,fi):14,(f,fi):10,(fi,six):2,(six,seven):1,(six,eight):6,(seven,eight):7}
g = Graph(v,e)
g.prim(z)
g.Dijkstra(z)

