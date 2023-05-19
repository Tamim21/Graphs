from Heap import Heap
class Graph:  # adj list
    def __init__(self, vs, es):
        self.vs = vs  # set of vertices {v,v,...}
        self.es = es  # dict of edges {(u,v) : weight}
        self.ass_neighbors()
    def ass_neighbors(self): # |E|
        for rec in self.es:
            rec[0].neighbors.add(rec[1])
            rec[1].neighbors.add(rec[0])
    def add(self,edge):
        self.es.add(edge)
        self.vs.add(edge.key[0])
        self.vs.add(edge.key[1])
        self.ass_neighbors()
    def prim(self, root): # V*getmin + E*update,,,,, V*lgv + E*lgv
        s = {node: [float("inf"), root] for node in self.vs}  # dict = node : (dist,parent)
        s[root] = [0, root]  # root: (dist = 0, parent = root)
        heap = Heap(s)  # vlgv
        s = {} # final answer
        while not (heap.isEmpty()):
            u = heap.extractMin()  # (node refrence,[dist,parent]), lgv
            n = u[0].neighbors
            s[(u[0],u[1][1])] = u[1][0] # {(n,p):dist}
            for v in n:
                if (u[0], v) in self.es and (v.posInHeap != -1):
                    if heap.array[v.posInHeap][1][0] > self.es[(u[0], v)]:
                        heap.array[v.posInHeap][1] = [self.es[(u[0], v)],u[0]]  # weight and parent update in the heap
                        heap.up_heapify(v.posInHeap) # update el heap
                elif (v, u[0]) in self.es and (v.posInHeap != -1) :
                    if heap.array[v.posInHeap][1][0] > self.es[(v,u[0])]:
                        heap.array[v.posInHeap][1] = [self.es[(v,u[0])], u[0]]
                        heap.up_heapify(v.posInHeap) # update el heap after minimizing weight
        root.parent = root
        del s[(root,root)]
        self.printMST(s)

    def printMST(self, s):
        print("- EDGE ------------ Weight")
        for i in s:
            print(f"{i[0].name} --- {i[1].name} ------------- {s[i]}")

    def Dijkstra(self, root):
        for e in self.es: # checking for negative edges
            if self.es[e] < 0:
                print("Dijkstra doesnt work with -ve weighted edges, try another algorithm!!!")
                return
        s = {node: [float("inf"), root] for node in self.vs}  # dict = node : (dist,parent)
        s[root] = [0, root]  # root: (dist = 0, parent = root)
        heap = Heap(s)  # vlgv
        s = {}
        while not (heap.isEmpty()):
            dist = heap.array[0][1][0]
            u = heap.extractMin()  # (node refrence,[dist,parent]), lgn
            n = u[0].neighbors
            s[(u[0],u[1][1])] = u[1][0] # {(n,p):dist}
            for v in n: # iter in neighbors of v
                if (u[0], v) in self.es and (v.posInHeap != -1):
                    if heap.array[v.posInHeap][1][0] > self.es[(u[0], v)] + dist:
                        heap.array[v.posInHeap][1] = [self.es[(u[0], v)] + dist,u[0]]  # weight and parent update in the heap
                        v.parent = u[0]
                        heap.up_heapify(v.posInHeap) # update el heap
                elif (v, u[0]) in self.es and (v.posInHeap != -1) :
                    if heap.array[v.posInHeap][1][0] > self.es[(v,u[0])] + dist:
                        heap.array[v.posInHeap][1] = [self.es[(v,u[0])] + dist,u[0]]
                        v.parent = u[0]
                        heap.up_heapify(v.posInHeap) # update el heap after minimizing weight
        self.printSP(s,root)

    def printSP(self,s,source):
        for i in s:#{(n,p):dist}
            print(f"path for {i[0].name} is")
            x = i[0]
            dist = s[(x,x.parent)]
            path = " "
            while x != source:
                path += str("--" + str(x.name))
                x = x.parent
            path += str("--" + str(x.name))
            print(f"path = {path} ---- Distance = {dist}")

