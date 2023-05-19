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
edges = {(z,o):3,(z,th):8,(o,th):4,(o,f):1,(o,t):10,(o,fi):2,(t,fi):5,(th,f):5,(th,six):1,(f,six):4,(f,fi):2,(fi,six):7}
g = Graph(vertices,edges)
g.Dijkstra(z)



v = {z,o,t,th,f,fi,six}
e ={(z,o):2,(z,th):1,(o,th):3,(o,f):10,(t,z):4,(t,fi):5,(th,t):2,(th,f):7,(th,fi):8,(th,six):4,(f,six):6,(six,fi):1}
g = Graph(v,e)
g.prim(z)

