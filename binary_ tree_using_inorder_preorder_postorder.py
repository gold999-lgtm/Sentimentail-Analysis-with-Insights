class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
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