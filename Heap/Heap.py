class MinHeap:
    def __init__(self):
        self.mHeap = []
        
    def __parent(self, idx):
        return idx//2
    
    def __leftchild(self, idx):
        return (2*idx)
    
    def __rightchild(self, idx):
        return (2*idx)+1
    
    def __swap(self, i, j):
        self.mHeap[i-1], self.mHeap[j-1] = self.mHeap[j-1], self.mHeap[i-1]
    
    def __getValue(self):
        print("Enter the number to be inserted")
        return int(input())  
    
    def insert(self):
        value = self.__getValue()
        self.mHeap.append(value)
        curr = len(self.mHeap)
        while self.__parent(curr)-1 >= 0 and self.mHeap[curr-1] < self.mHeap[self.__parent(curr)-1]:
            self.__swap(curr, self.__parent(curr))
            curr = self.__parent(curr)
        
    def pop(self):
        if not self.mHeap:
            print("Heap is empty")
            
        self.mHeap[0], self.mHeap[-1] = self.mHeap[-1], self.mHeap[0]
    
        minele = self.mHeap.pop()
        l = 1
        while l<=len(self.mHeap):
            leftchild = self.__leftchild(l)
            rightchild = self.__rightchild(l)
            smallest = l
            if  leftchild<=len(self.mHeap) and self.mHeap[smallest-1] > self.mHeap[leftchild-1]:
                smallest = leftchild
            if rightchild<=len(self.mHeap) and self.mHeap[smallest-1] > self.mHeap[rightchild-1]:
                smallest = rightchild
            if smallest == l:
                break
            self.__swap(smallest, l)
            l = smallest
        return minele    
        
    def heapSort(self):
        heapsort = []
        while self.mHeap:
            heapsort.append(self.pop()) 
        print(*heapsort)
        
    def display(self):
        print(*self.mHeap)
             
if __name__ == "__main__":
    o = MinHeap()
    insert = True
    while insert:
        o.insert()
        print("Enter F if you want to stop inserting")
        if input().lower() == "f":
            insert = False
    o.display()
    # print(o.pop())
    # o.display()
    o.heapSort()

