class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.start=None
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
    def addlevelorder(self,value):
        if self.start==None:
            self.start=node(value)
        else:
            self._addlevelorder(self.start,value)
    def _addlevelorder(self,current,value):
        queue=[]
        queue.append(current)
        while len(queue)>0:
            node1=queue.pop(0)
            if node1.left:
                queue.append(node1.left)
            if node1.right:
                queue.append(node1.right)
            if node1.left==None:
                node1.left=node(value)
                return
            if node1.right==None:
                node1.right=node(value)
                return
            
                
            

ob1=tree()
first=node(1)
second=node(2)
third=node(3)
fourth=node(4)
fifth=node(5)
sixth=node(6)
seventh=node(7)
ob1.start=first
first.left=second
first.right=third
second.left=fourth
second.right=fifth
third.left=sixth
third.right=seventh
print("Inorder",end=" ")
ob1.inorder()
print(" ")
print("Preorder",end=" ")
ob1.preorder()
print(" ")
print("Postorder",end=" ")
ob1.postorder()
print(" ")
print("levelorder",end=" ")
ob1.levelorder()
ob1.addlevelorder(8)
print("levelorder",end=" ")
ob1.levelorder()