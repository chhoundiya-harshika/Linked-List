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
            temp.next=new_node #doubly requirement node add to the last
            new_node.prev=temp #doubly requirement
        else:
            self.head=new_node
            
    def insert(self,new_node, pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            p=1
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.prev=temp
            new_node.next = temp.next
            temp.next=new_node
            if temp.next: #this is for last pos
                temp.next.prev=new_node
                
    # def print(self):
    #             temp=self.head
    #             print("List elements: ")
    #             while temp:
    #                 print(temp.data," ")
    #                 temp=temp.next
        #for reverse the list element
        
    # def delete(self, value):
    #     temp=self.head
    #     prev = None
    #     if temp.data==value: #first node
    #         self.head=self.head.next
    #         self.head.prev= None
    #     else:
    #         while(temp.data!= value and temp):
    #             temp=temp.next
    #             if temp==None:
    #                 print("Value is not present in the list:")
    #                 return
    #             temp.prev.next=temp.prev
    #             if temp.next: #not the last node
    #                 temp.next.prev=temp.prev #last node delete
    #             temp=None
                
    def occurance(self, num):
        temp=self.head
        count=0
        while temp :
            if temp.data==num:
                count+=1
            temp=temp.next
        print("The occurances", count)
                  
            
    def print(self):
        temp=self.head
        print("List elements: ")
        while temp:
           # print(temp.data," ")
            temp=temp.next
        while (temp):
            print(temp.data, end=" ")
            temp=temp.prev
            
list1=LinkedList()
list1.append(Node(10))       
list1.append(Node(12))       
list1.append(Node(14))       
list1.append(Node(16))       
list1.append(Node(18))      
list1.print()
list1.insert(Node(5),1) 
list1.insert(Node(15),3) 
list1.insert(Node(45),8) 
list1.print()
# list1.delete(12)
list1.occurance(12)
