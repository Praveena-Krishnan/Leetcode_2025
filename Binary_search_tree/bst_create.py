class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
        
class Tree:
    def create(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.craete(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        elif data>node.data:
            node.right=self.insert(node.right,data)
        return node