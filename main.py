
class vertex:
    Names = []
    def __init__(self,name):
        warning = ''
        while name in vertex.Names:
            input("please "+ warning +" input a unique name to the vertex " + str(name))
            warning = 'ya 8abyy'
        vertex.Names.append(name)
        self.neighbors = set({})  # set  of neighbors {v,v,v}
        self.name = name
        self.posInHeap = -1
        self.parent = None
class Heap():

    def __init__(self, dict):
        self.array = []  # array of recs (node , [dist,parent]), key of comparison is a[i][1][0]
        self.size = 0
        for v in list(dict.keys()):
            self.array.append([v,dict[v]])
            v.posInHeap = self.size
            self.size += 1
        self.build_min_heap()

    def build_min_heap(self): #nlgn
        last_parent = (self.size - 2) // 2
        for i in range(last_parent, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, index): #max lgn
        left = 2 * index + 1
        right = left + 1
        if right < self.size :
            mn = min(self.array[index][1][0], self.array[left][1][0], self.array[right][1][0])
            if mn == self.array[index][1][0]:
                return
            elif mn == self.array[left][1][0]:
                self.array[index][0].posInHeap,self.array[left][0].posInHeap = self.array[left][0].posInHeap , self.array[index][0].posInHeap
                self.array[index], self.array[left] = self.array[left], self.array[index]
                self.min_heapify(left)
            else:
                self.array[index][0].posInHeap, self.array[right][0].posInHeap = self.array[right][0].posInHeap, self.array[index][0].posInHeap
                self.array[index], self.array[right] = self.array[right], self.array[index]
                self.min_heapify(right)
        elif left < self.size:
            mn = min(self.array[index][1][0], self.array[left][1][0])
            if mn == self.array[index][1][0]:
                return
            elif mn == self.array[left][1][0]:
                self.array[index][0].posInHeap, self.array[left][0].posInHeap = self.array[left][0].posInHeap, self.array[index][0].posInHeap
                self.array[index], self.array[left] = self.array[left], self.array[index]
                self.min_heapify(left)
    def up_heapify(self,index): #max lgn
        if index == 0:
            return
        else:
            parent = (index - 1)//2
            if self.array[index][1][0] < self.array[parent][1][0]:
                self.array[index][0].posInHeap,self.array[parent][0].posInHeap = parent,index
                self.array[index], self.array[parent] = self.array[parent], self.array[index]
                self.up_heapify(parent)
            else:
                return



    def extractMin(self): #lgn

        if self.isEmpty() == True:
            return

        min = self.array[0]
        last = self.array[self.size - 1]
        self.array[0] = last
        self.array[self.size-1] = min
        last[0].posInHeap = 0
        min[0].posInHeap = -1
        self.size -= 1
        self.array.remove(min)
        self.min_heapify(0)

        return min

    def isEmpty(self): # 1
        return True if self.size == 0 else False



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

