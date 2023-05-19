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