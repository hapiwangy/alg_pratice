class Algs:
    '''
        implementation of different algorithms
    '''
    def __init__(self) -> None:
        self.test = [4, 3, 5, 2, 1, 6, 100, 7]
        self.llen = len(self.test)
    def bubble_sort(self):
        '''
            implementation of bubble_sort
            time compplexity: O(n^2)
            space complexity: O(1)
        '''
        for _ in range(self.llen):
            for x in range(self.llen - 1):
                if self.test[x] > self.test[x + 1]:
                    self.test[x], self.test[x + 1] = self.test[x + 1], self.test[x]
    def cocktail_sort(self):
        '''
            implementation of cocktail_sort
            time compplexity: O(n^2) / average might be O(n)
            space complexity: O(1)
        '''
        is_sorted = True
        start = 0
        end = self.llen - 1
        while is_sorted:
            is_sorted = False
            for x in range(start, end):
                if self.test[x] > self.test[x + 1]:
                    self.test[x], self.test[x + 1] = self.test[x + 1], self.test[x]
                    is_sorted = True
            print("往後排序的過程: ", self.test)
            if not is_sorted:
                # 沒有交換的時候代表可以跳出迴圈(已經排好了)
                break     
            end = end - 1
            for x in range(end - 1, start - 1, -1):
                if self.test[x] > self.test[x + 1]:
                    self.test[x], self.test[x + 1] = self.test[x + 1], self.test[x]
                    is_sorted = True
            start = start + 1
            print("往前排序的過程: ", self.test)
    
    def selection_sort(self):
        '''
            implementation of selection_sort
            time compplexity: O(n^2)
            space complexity: O(1)            
        '''
        for x in range(self.llen - 1):
            min_index = x
            for i in range(x + 1, self.llen):
                if self.test[min_index] > self.test[i]:min_index = i
            if min_index == x:
                pass
            else:
                self.test[min_index], self.test[x] = self.test[x], self.test[min_index]
    def insertion_sort(self):
        '''
            implementation of insertion_sort
            time compplexity: O(n^2)
            space complexity: O(1)            
        '''
        for i in range(1, self.llen):
            for x in range(i, 0, -1):
                if self.test[x] < self.test[x - 1]:
                    self.test[x], self.test[x - 1] = self.test[x - 1], self.test[x]
                else:
                    break     
    def heap_sort(self):
        '''
            implementation of heap_sort
            insert / takeout element from heap is o(logn)(time complexity) 
            time compplexity: O(nlogn)
            space complexity: O(1)    
            we have to build heap tree frist than we can do sorting
            we build tree first, than take out data from it. than we finish our sorting    
        '''    
        import heap_tree
        htree = heap_tree.Heaptree()
        htree.build_heap(self.test)
        print("finish build heap tree: ", htree.heap)
        self.test = []
        for i in range(self.llen):
            self.test.append(htree.get_min())
    def do_quick_sort(self):
        '''
        call the quick_sort function
        '''
        nlist = self.test
        self.test = self.quick_sort(nlist)
    def quick_sort(self, nlist):
        '''
            implementation of quick_sort
            time compplexity: O(nlogn)
            space complexity: O(1)   
        '''
        import random
        if len(nlist) <= 1:return nlist
        left = []
        right = []
        piv = []
        pivot = random.choice(nlist)
        for val in nlist:
            if val == pivot:
                piv.append(val)
            elif val < pivot:
                left.append(val)
            elif val > pivot:
                right.append(val)
        return self.quick_sort(left) + piv + self.quick_sort(right)
    
    def do_merge_sort(self):
        nlist = self.test
        self.test = self.merge_sort(nlist)
    def merge(self, left,  right):
        ''' merger left and right'''
        output = []
        while left and right:
            if left[0] < right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        if left: output += left 
        else: output += right
        return output
    def merge_sort(self, nlist):
        '''
            implementation of merge sort
            time complexity O(nlogn)
            space complexity O(n)
        '''
        if len(nlist) <= 1: return nlist
        mid = len(nlist) // 2
        # divide sequence
        left = nlist[:mid]
        right = nlist[mid:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)

    def binary_search(self, key_value):
        self.test.sort()
        low = 0
        high = self.llen
        middle = int((low+high) / 2)
        times = 0
        while True:
            times += 1
            if key_value == self.test[middle]:
                rtn = middle
                break
            elif key_value > self.test[middle]:
                low = middle + 1
            else:
                high = middle - 1
            middle = int((low+high) / 2)
            if low > high:
                rtn = -1
                break
        return rtn, times
    def __repr__(self):
        strs = " ".join([str(x) for x in self.test])
        strs = f"排序完的列表是: {strs}"
        return strs