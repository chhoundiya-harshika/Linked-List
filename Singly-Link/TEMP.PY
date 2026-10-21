class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
        print("Appending element:")
    def traverse(self):
        temp=self.head
    while temp:
        print(temp.data)
    temp=temp.next

    def insert(self, new_node, pos):
        if pos==1:
            new_node.next=self.head
            self.head=new_node
        else:
            temp=self.head
            p=1
        while p<pos-1 and temp!=None:
            P+=1
        if temp!=None:
            new_node.next=temp.next
        temp.next=new_node
    def delete(self):
        temp = self.head
        prev=None
        if(temp.data<0):
            self.head=self.head.next
        temp=self.head
        while temp:
            if(temp.data<0):
                prev.next=temp.next
                t=temp
            else:
                prev=temp
            temp=temp.next
list=LinkedList()
list.append(Node(-50))
list.append(Node(-10))
list.append(Node(-20))
list.append(Node(40))
print("")
list.traverse()
list.insert(Node(30),2)
print("Insert element at specific position:")
list.traverse()
list.delete()
print("delete negative nodes:")