#Chapter 9 Problems: 1,2,4,10,11,12,15
#Completed: 1,2,3,10,11,

'''Binary Trees Bootcamp'''

'''
9.1  Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:

    def dfs(root):
        
        if not root: return [True, 0]
        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] -  right[1]) <= 1
        
        return [balanced, 1 + max(left[1], right[1])]
                
    return dfs(root)[0]

'''9.2 Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
  def isSymmetric(left, right):
      if not left and not right:
          return left == right
      
      elif left and right:
          return (left.val == right.val and 
                  isSymmetric(left.left, right.right) and
                  isSymmetric(left.right, right.left))

      return False

  
  return not root or isSymmetric(root.left, root.right)


'''
9.3 LCA: Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”'''

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  cur = root
  while cur:
      if p.val > cur.val and q.val > cur.val:
          cur = cur.right
      elif p.val < cur.val and q.val < cur.val:
          cur = cur.left
      else:
          return cur



'''
9.10 Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.'''

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
  if not root: return None
  res = []
  
  def inorder(root):
      if not root: return
      
      inorder(root.left)
      res.append(root.val)
      inorder(root.right)

  inorder(root)
  return res

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
    res = []
    stack = []
    cur = root 
    
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
            
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
        
    return res

'''
9.11 Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal 
of a binary tree and inorder is the inorder traversal of the same tree, construct and
return the binary tree. '''

def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
  if not inorder or not preorder:
      return None
  
  root = TreeNode(preorder[0])
  mid = inorder.index(preorder[0])
  
  root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
  root.right = self.buildTree(preorder[1+mid:], inorder[1+mid:])
  
  return root

