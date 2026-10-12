class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        
    def Enqueue(self,value):
        if (self.rear+1) % self.size==self.front:
            print("Queue Overflow")
        
         
        elif self.front==-1:
                self.front=0
                self.rear=0
                self.queue[self.rear]=value
                print(value,"inserted in the queue")
        else:
                self.rear = (self.rear+1) % self.size
                self.queue[self.rear] = value
                print(value,"inserted in the queue")
                
    def Dequeue(self):
        if self.front==-1:
            print("Queue  Underflow")
        else:
            value =self.queue[self.front]
            self.queue[self.front]=None
            
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            else:
                self.front=(self.front+1) % self.size        
            print(value,"removed from Queue")
    
    def Peek(self):
        if self.front==-1:
            print("Queue is Empty")
        else:
            print("Front Element:",self.queue[self.front])
    
    def display(self):
        if self.front==-1:
            print("Queue is Empty")
        else:
            i=self.front
            while True:
                print(self.queue[i],end=" ")
                if i==self.rear:
                    break
                i=(i+1)%self.size
            print()                
q=CircularQueue(5)  
    
q.Enqueue(10)
q.Enqueue(20)  
q.Enqueue(30) 
q.Enqueue(40)

    
q.display()
q.Peek()
    
q.Dequeue()
q.Dequeue()
    
q.Enqueue(50) 
q.Enqueue(60) 
q.Enqueue(70)    
q.display()                  
        


