#Chapter 14 Problems: 1,2,3,4; 5,8,7
#Completed: 1,2,3,4,5

'''Binary Search Trees Bootcamp'''

'''
The following program demonstrates how to check if a given value is present in a BST.
It is a nice illustration of the power of recursion when operating on BSTs'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    if root is None or val == root.val:
        return root
    
    return self.searchBST(root.left, val) if val < root.val \
        else self.searchBST(root.right, val)

'''
bintrees module

insert(e): inserts new element e in the BST
discard(e): removes e in the BST if present
min_item()/max_item() yield the smallest and largest key-value pair in the BST
min_key()/max_key(): yield the smallest and largest ket in the BST
pop_min()/pop_max(): remove the return the smallest and largest key-value pair in the BST.
'''
    
'''
14.1 Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def valid(root, left, right):
        if not root:
            return True
        
        if not (left < root.val < right):
            return False
        
        return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        
    return valid(root, float('-inf'), float('inf'))


'''
14.2 Find the first key greater than a given in a BST

Write a program that takes as input a BST and a value, and returns the first key that would appear
in an inorder traversla which is greater than the input value. For example, when applied in the BST
'''
      
import sys
sys.path.append("./mylib")
import BST

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,10,7,6,9,12,15]
for x in input:
    BST.insert(root, BST.BSTNode(x))


def nextNode(node,target):
    result = None
    while node:
        #if value > target, can be successor!
        if node.data > target:
            result = node.data
            #IMPORTANT: find smallest of the largest!
            node = node.left
        else:
            #go right!
            node = node.right
    return result

target = 11
print("First value greater than ", target , " = ", nextNode(root,target))


'''
14.3 kth smallest element in BST
Given the root of a binary search tree, and an integer k, return the kth smallest value 
(1-indexed) of all the values of the nodes in the tree.'''

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    res = []
    cur = root

    while cur or stack:

        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
        
        if len(res)-1 == k - 1:
            return res[-1]


'''
14.4 Compute the LCA in a BST

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p
 and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
    if not root: return None
    cur = root
    
    while cur:
        
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right 
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
            
        else:
            return cur

'''
14.5 BST from preorder traversal

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.'''

def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    
    def helper(lower = float('-inf'), upper = float("inf")):
        nonlocal idx
    
    
        if idx == n: return None
        val = preorder[idx]
        if val < lower or val > upper:
            return None

        idx += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)

        return root
    
    idx = 0
    n = len(preorder)
    
    return helper()


'''
Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:

'''

def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    
    p1, p2 = p, q
    while p1 != p2:
        p1 = p1.parent if p1.parent else q
        p2 = p2.parent if p2.parent else p
        
    return p1


''' 
Reconstruct Iternary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.'''

def findItinerary(self, tickets: List[List[str]]) -> List[str]:

    adj = { src: [] for src, dest in tickets }
    tickets.sort()

    for src, dest in tickets:
        adj[src].append(dest)

    res = ["JFK"]

    def dfs(src):
        if len(res) == len(tickets) + 1:
            return True
        if src not in adj:
            return False
        
        temp = list(adj[src])

        for i, v in enumerate(temp):
            adj[src].pop(i)
            res.append(v)
            if dfs(v): return True
            adj[src].insert(i, v)
            res.pop()
        return False

    dfs('JFK')
    return res


'''
All Paths from source to destination

'''

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

    target = len(graph) - 1
    results = []

    def backtrack(curr_node, path):
        # if we reach the target, no need to explore further.
        if curr_node == target:
            results.append(list(path))
            return
        # explore the neighbor nodes one after another.
        for next_node in graph[curr_node]:
            path.append(next_node)
            backtrack(next_node, path)
            path.pop()
    # kick of the backtracking, starting from the source node (0).
    path = [0]
    backtrack(0, path)

    return results