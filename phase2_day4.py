#creation of Tree

class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder()

    def insert(self,data):
        if self.data > data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)
                
    def remove(self,node,x):
        if node is None:
            return node
        if x<node.data:
            root.left=self.remove(node.left,x)
        elif x>node.data:
            root.right=self.remove(node.right,x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data=self.min(node.right)
            node.right=self.remove(node.right,node.data)
        return node

    def preorder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")

    def find(self,node,x):
        if node is None:
            return
        if node.data==x:
             print("Found")
             return 1
        self.find(node.left,x)
        self.find(node.right,x)
        
            
    def min(self,node):
        while node.left:
            node=node.left
        return node.data
        
    def max(self,node):
        while node.right:
            node=node.right
        return node.data

    def height(self,node):
        if node is None:
            return -1
        else:
            ldepth=self.height(node.left)
            rdepth=self.height(node.right)
            if ldepth>rdepth:
                return ldepth+1
            else:
                return rdepth+1
                    
root=Node(20)
root.insert(30)
root.insert(10)
root.insert(4)
root.insert(24)
root.insert(28)
root.insert(8)
root.insert(5)
root.insert(2)
print("the tree in inorder:")
root.inorder()
print("\nthe Tree in pre order:")
root.preorder(root)
print("\nthe tree in post order:")
root.postorder(root)
print("\nThe min of tree :",root.min(root))
print("The max of tree : ",root.max(root))
print("14 is present in tree:",end=" ")
if root.find(root,14) is None:
    print("Not Found")
root.remove(root,4)
print("the tree after removing 4 in inorder:")
root.inorder()
print("\nthe height of tree:",root.height(root))
