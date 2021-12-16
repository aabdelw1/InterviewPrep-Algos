def height(root):
    if not root:
        return -1
    
    else:
        left = height(root.left)
        right = height(root.right)
        return(max(left, right) +1)

def height(root):
    add = 0
    if root.left:
        add = 1 + height(root.left)
    if root.right:
        add = 1 + height(root.right)
    
    return add

def height(root):
    if not root:
        return -1
    return max(height(root.left), height(root.right)) + 1