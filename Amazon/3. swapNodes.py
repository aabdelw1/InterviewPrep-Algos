import os
import sys
from collections import deque
sys.setrecursionlimit(10000)


#create node class

class Node:
  #constructor
  def __init__(self, val) -> None:
      self.info = val
      self.left = None
      self.right = None
      
def swapNodes(indexes, queries):
  def create(root, indexes):
    q = deque([root])
    #traverse the indexes
    for x,y in indexes:
      #pop the element from the q
      temp = q.popleft()
        #left child
      if x != -1:
        temp.left = Node(x)
        q.append(temp.left)
      
      #right child
      if y != -1:
        temp.right = Node(y)
        q.append(temp.right)

    return root

  def swap(root, k, level, l):
    if root:
      #if it is a multiple of k swap the nodes
      if level%k == 0:
        root.left, root.right = root.right, root.left

      #inorder traversal
      swap(root.left, k, level+1, l)
      l.append(root.info)
      swap(root.right, k, level+1, l)

  #create root node
  root = Node(1)
  #create the tree from indexes
  root = create(root, indexes)

  result = []
  #process the queries
  for k in queries:
    l = []
    swap(root, k,  1, l)
    result.append(l)

  return result