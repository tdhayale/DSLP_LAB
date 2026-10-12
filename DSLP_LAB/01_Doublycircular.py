class Node:
    def __init__(self,data):
        self.data = data
        self.prev=None
        self.next=None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        new_node= Node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        

        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        new_node.prev=temp

    def display_forward(self):
        temp=self.head

        while temp is not None:
            print(temp.data,end="<->")
            temp=temp.next

        print("None")   

    def display_backward(self):
        if self.head is None:
            print("Empty")
            return

        temp=self.head
        while temp.next is not None:
            temp=temp.next

        while temp is not None:
            print(temp.data,end="<->")   
            temp=temp.prev
        print("None")

dcl=DoublyCircularLinkedList()
dcl.insert_end(10)
dcl.insert_end(20)
dcl.insert_end(30)
dcl.display_forward()



