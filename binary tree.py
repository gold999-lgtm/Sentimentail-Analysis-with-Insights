class node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.root=None
        self.par=None
        
class tree:
    def __init__(self):
        self.start=None
        global c
        c=0
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
    def search (self,key):
        global c
        c=0
        item=node(key)
        if self.start==None:
            print("Tree is empty")
        else:
            ptr=self.start
            if ptr.data==item.data:
                print("Item is found at",c)
            elif ptr.data>item.data:
                c=2*c+1
                ptr=ptr.left
                self._search(ptr,key,c)
            elif ptr.data<item.data:
                c=2*c+2
                ptr=ptr.right
                self._search(ptr,key,c)
    def _search(self,ptr,key,c):
        item=node(key)
        if ptr.data==item.data:
            print("Item is found at",c)
        elif ptr.data>item.data:
            c=2*c+1
            ptr=ptr.left
            self._search(ptr,key,c)
        elif ptr.data<item.data:
               c=2*c+2
               ptr=ptr.right
               self._search(ptr,key,c)  
    def deletenode(self,key):
        item=node(key)
        ptr=self.start
        if ptr==None:
            print("Tree is empty")
        else:
            if ptr.data==item.data:
                if ptr.left==None and ptr.right!=None:
                    ptr.data=ptr.right.data
                    
                elif ptr.right==None and ptr.left!=None:
                    ptr.data=ptr.left.data
                    
                elif ptr.right!=None and ptr.left!=None:
                    ptr.data=ptr.right.data
                    ptr=ptr.right
                    ptr.data=ptr.right.data
                    
                    
                elif ptr.left==None and ptr.right==None:
                    ptr.data=None
                    
                
            elif ptr.data<item.data:
                self._deletenode(ptr.right,key)
                
                    
               
                    
            elif ptr.data>item.data:
                self._deletenode(ptr.left,key)
                
    def _deletenode(self,ptr,key):
        item=node(key)
        if ptr.data==item.data:
                if ptr.left==None and ptr.right!=None:
                    ptr.data=ptr.right.data
                    
                elif ptr.right==None and ptr.left!=None:
                    ptr.data=ptr.left.data
                    
                elif ptr.right!=None and ptr.left!=None:
                    ptr.data=ptr.right.data
                    ptr.right=ptr.right.right
                    
                    
                elif ptr.left==None and ptr.right==None:
                    ptr.data=None
                    
        elif ptr.data<item.data:
                self._deletenode(ptr.right,key)
            
        elif ptr.data>item.data:
                self._deletenode(ptr.left,key)
    def insert_node(self,key,loc):
        c=0
        item=node(key)
        par=self.start
        while par:
            if loc==c:
                if par.data>item.data:
                   
                    item.right=node(par.data)
                    item.left=None
                    par.data=item.data
                    break
                elif par.data<item.data:
                    item.left=node(par.data)
                    item.right=None
                    par.data=item.data
                    break
                    
                
            elif par.data>item.data: 
                par=par.left
                c=2*c+1
            elif par.data<item.data:
                par=par.right
                c=2*c+2
                
           
            
               
               
            
            
       
        
   
        
            
           
           
              
           
            
        
                
   
        
        
                
    
                
ob1=tree()
first=node(21)
second=node(9)
third=node(30)
fourth=node(6)
fifth=node(11)
sixth=node(28)
seventh=node(40)
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


ob1.insert_node(26,2)
print(" ")
ob1.inorder()

