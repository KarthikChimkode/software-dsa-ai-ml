# Foundation (Binary Tree basic)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode('A')
root.left = TreeNode('B')
root.righ   t = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')

def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if not root:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

def insert(root, val):
    
inorder(root)
preorder(root)
postorder(root)