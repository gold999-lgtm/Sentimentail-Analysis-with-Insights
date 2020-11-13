class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class binarysearchtree:
    def __init__(self):
        self.start=None
    def inorder(self):
        if (self.start==None):
            print("Tree is empty")
        else:
            self._inorder(self.start)
    def _inorder(self,current):
        if(current):
            self._inorder(current.left)
            print(current.data,end=" ")
            self._inorder(current.right)
    def preorder(self):
        if (self.start==None):
            print("Tree is empty")
        else:
            self._preorder(self.start)
    def _preorder(self,current):
        if(current):
            print(current.data,end=" ")
            self._preorder(current.left)
           
            self._preorder(current.right)
    def postorder(self):
        if (self.start==None):
            print("Tree is empty")
        else:
            self._postorder(self.start)
    def _postorder(self,current):
        if(current):
            self._postorder(current.left)
            self._postorder(current.right)
            print(current.data,end=" ")
    def addnode(self,value):
        if(self.start==None):
            self.start=node(value)
        else:
            self._addnode(self.start,value)
    def _addnode(self,current,value):
        if current.data>value:
            if current.left==None:
                current.left=node(value)
            else:
                self._addnode(current.left,value)
        elif current.data<value:
            if current.right==None:
                current.right=node(value)
            else:
                self._addnode(current.right,value)
        else:
            print("Value is already aaded in tree")
    def levelorder(self):
        if (self.start==None):
            print("Tree is empty")
        else:
            self._levelorder(self.start)
    def _levelorder(self,current):
        queue=[]
        queue.append(current)
        while len(queue)>0:
            node1=queue.pop(0)
            print(node1.data,end=" ")
            
            if(node1.left):
                queue.append(node1.left)
            if(node1.right):
                queue.append(node1.right)
    
            
ob1=binarysearchtree()
ob1.addnode(10)
ob1.addnode(5)
ob1.addnode(15)
ob1.addnode(2)
ob1.inorder()
print(" ")
ob1.preorder()
print(" ")
ob1.postorder()
print(" ")
ob1.inorder()
print(" ")
