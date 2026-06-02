class Node:
    def __init__(self,item):
        self.info=item
        self.right=None
        self.left=None
class BinarySTree:
    def __init__(self):
        self.root=None
    def insert(self,item):
        nd=Node(item)
        if self.root==None:
            self.root=nd
            return
        temp=self.root
        while temp!=None:
            if item<temp.info:
                par=temp
                temp=temp.left
            else:
                par=temp
                temp=temp.right
        if item<par.info:
            par.left=nd
        else:
            par.right=nd
    def inorder(self, nd):
        if nd!=None:
            self.inorder(nd.left)
            print(nd.info)
            self.inorder(nd.right) 
obj=BinarySTree()
obj.insert(10)
obj.insert(5)
obj.insert(15)
obj.insert(3)
obj.insert(7)
obj.inorder(obj.root)