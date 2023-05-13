class Heaptree():
    '''
        heap tree implementation
    '''
    def __init__(self,):
        self.heap = []
        self.size = 0

    def data_down(self, i):
        '''
            if node value > child node, 
                node value change with smaller child node
        '''
        while (i * 2 + 2) <= self.size:
            mi = self.get_min_index(i)
            if self.heap[i] > self.heap[mi]:
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]
            i = mi

    def get_min_index(self, i):
        '''return miniest child node'''
        if i * 2 + 2 >= self.size:
            return i * 2 + 1
        else:
            if self.heap[i * 2 + 1] < self.heap[i * 2+2]:
                return i * 2 + 1
            else:
                return i * 2 + 2
            
    def build_heap(self, mylist):
        '''建立 heaptree'''
        i = (len(mylist) // 2) - 1
        self.size = len(mylist)
        self.heap = mylist
        while (i >= 0):
            self.data_down(i)
            i = i - 1
    def get_min(self):
        min_ret = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        self.data_down(0)
        return min_ret