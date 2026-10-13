class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top=None

    #Push: O(1)
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

    #Pop: O(1)
    def pop(self):
        if self.top is None:
            print("Stack is Empty!")
            return None
        removed_value=self.top.data
        self.top=self.top.next
        return removed_value

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return None
        return self.top.data
    def display(self):
        current= self.top
        if current is None:
            print("Stack is Empty")
            return
        while current is not None:
            print(current.data)
            current=current.next

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack elements (Top to Bottom):")
s.display()
print("Top Element:",s.peek())
print("POP Element:",s.pop())
print("Stack after POP:")
s.display()
