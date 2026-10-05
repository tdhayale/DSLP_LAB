class Node:
    def __init__(self,data):
       self.data=data
       self.next=None

class CircularLinkedList:
   def __init__(self):
      self.head=None

   def insert_end(self,data):
       new_node=Node(data)

       if self.head is None:
         self.head=new_node
         new_node.next=self.head
         return
      

       temp=self.head

       while temp.next !=self.head:
         temp=temp.next

       temp.next=new_node
       new_node.next=self.head

   def display(self):
      if self.head is None:
         print("Empty")
         return
      temp=self.head

      while True:
         print(temp.data,end=" ->")
         temp=temp.next

         if temp==self.head:
            break
      print("(back to Head)")

   def delete_first(self):
      if self.head is None:
         print("Empty")
         return
      
      if self.head.next==self.head:
         self.head=None
         return
      temp=self.head

      while temp.next!=self.head:
         temp=temp.next

      self.head=self.head.next

      temp.next=self.head   

      temp=self.head
      temp.next=self.head.next

      
        

cll=CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.display()
cll.delete_first()
cll.display()
       

