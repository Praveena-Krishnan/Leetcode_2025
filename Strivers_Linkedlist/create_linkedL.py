class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next = new_node
    
    def insert_index(self,data,index):
        new_node=Node(data)
        if index==0:
            self.insert_beg(data)
        count=0
        current_node=self.head
        while current_node and count+1!=index:
            count+=1
            current_node=current_node.next
            
        if current_node is None:
            print("Index out of bounds")
        else:
            new_node.next=current_node.next
            current_node.next=new_node
            
    def delete_beg(self):
        if self.head==None:
            print("list is empty")
            return
        else:
            self.head=self.head.next
    
    def delete_end(self):
        if self.head==None:
            print("lsit is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        current_node=self.head
        while current_node.next and current_node.next.next:
            current_node=current_node.next
        current_node.next=None
            
        
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" => ")
            current_node = current_node.next
        print("None")

llist=LinkedList()
llist.insert_end(1)
llist.insert_end(2)
llist.insert_end(3)
llist.insert_end(4)
llist.insert_index(5,3)
llist.delete_beg()
llist.delete_end()
llist.print_list()
    
            
            
