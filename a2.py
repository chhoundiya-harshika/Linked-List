class Node:
    def __init__(self):
        self.data = val
        self.next = None
class LinkedList:
    def append (self, new_node):
        if(self.head==None):
            temp.next = new_node
        else:
            temp = self.head
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next.next
list = LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)        
list.append(n2)        
list.append(n3)        
list.append(Node(40)) 
list.print()       
       