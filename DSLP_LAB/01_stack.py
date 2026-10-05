class Stack:
    
    def __init__(self,size):
        self.size = size
        self.stack = [None]*size
        self.top = -1
    
    def push(self,value):
        if self.top==self.size-1:
            print("Stack Overflow")
        else:
            self.top=self.top+1
            self.stack[self.top]=value
            print(value,"pushed into stack")
            
    def pop(self):
        if  self.top==-1:
            print("Stack Underflow")
        else:
            value=self.stack[self.top]
            self.top=self.top-1
            print(value,"popped from stack")
    
    def peek(self):
        if self.top==-1:
            print("Stack is Empty")
        else:
            print("Top element:",self.stack[self.top])
              
    def display(self):
        if self.top==-1:
            print("Stack is Empty")
        else:
            print("Stack Elements:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])  
                
stack = Stack(5)

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()
stack.peek()
stack.pop()     

                                         