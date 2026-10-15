class Node:
    def __init__(self, value):
        self.prev=None
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next: #finding last node
                temp=temp.next
            temp.next=new_node #doubly requirement add to
            new_node.prev=temp #doubly requirement
        else:
            self.head=new_node
    def print(self):
        temp=self.head
        print("List elements: ")
        while temp:
            print(temp.data," ")
            temp=temp.next
list1=LinkedList()
list1.append(Node(10))       
list1.append(Node(12))       
list1.append(Node(14))       
list1.append(Node(16))       
list1.append(Node(18))       
list1.print()