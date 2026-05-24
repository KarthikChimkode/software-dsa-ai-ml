from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

"""
        A
      /   \
     B     C
    / \
   D   E



inorder('A')
    inorder('B')
        inorder('D')
            inorder(None)     # No left child
            prints('D')
            inorder(None)     # No right child
        prints('B')
        inorder('E')
            inorder(None)     # No left child
            prints('E')
            inorder(None)     # No right child
    prints('A')
    inorder('C')
        inorder(None)         # No left child
        prints('C')
        inorder(None)         # No right child



"""