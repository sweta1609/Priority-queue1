class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
    
    def __percolateDown(self):
        parentIndex = 0 #intially parent index is 0
        leftchildindex = 2*parentIndex + 1
        rightchildindex = 2*parentIndex + 2
        while leftchildindex < self.getSize(): #tht means left child index is less then legth of array
            minIndex = parentIndex #initially parent index is minimum
            if self.pq[minIndex].priority > self.pq[leftchildindex].priority: #if minindex priority is greater then leftchild index priority then minindex will be equal to leftchild
                minIndex = leftchildindex
            if rightchildindex <self.getSize() and self.pq[minIndex].priority > self.pq[rightchildindex].priority:#before comparing we should check if rightchild index exist within size or not
                minIndex = rightchildindex
            if minIndex == parentIndex:
                break
                
            self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
            parentIndex = minIndex
            leftchildindex = 2*parentIndex + 1
            rightchildindex = 2*parentIndex + 2
            
        
        
    def removeMin(self):
        if self.isEmpty():
            return None
        ele =self.pq[0].ele #stores element a 0th index 
        self.pq[0] =self.pq[self.getSize()-1] #stores last element at 0th index
        self.pq.pop() #it will remove last element
        self.__percolateDown() #while removing lement we move in downward direction
        return ele
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    
