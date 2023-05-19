class vertex:
    Names = []
    def __init__(self,name):
        warning = ''
        while name in vertex.Names:
            input("please ,"+ warning +" input a unique name to the vertex " + str(name))
            warning = 'ya 8abyy'
        vertex.Names.append(name)
        self.neighbors = set({})  # set  of neighbors {v,v,v}
        self.name = name
        self.posInHeap = -1
        self.parent = None
    def clearNeighbors(self):
        self.neighbors = set({})