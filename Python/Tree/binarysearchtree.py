class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None 


def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root 

def search(root, val):
    if not root or root.val == val:
        return root 
    
    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)
    
def find_min(root):
    while root.left:
        root = root.left
    return root 

def delete(root, val):
    if not root:
        return root 
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)

    else:
        #case 1: no child
        if not root.left and not root.right:
            return None 
        
        #case 2: one child
        if not root.left:
            return root.right
        if not root.right:
            return root.right
        
        #case 3 two children
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root 

