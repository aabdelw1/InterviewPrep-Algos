#Chapter 8 Problems: 1,2,3,4,6,7,8
#Completed: 1,2,3,4,6,8

'''Stacks Bootcamp'''

import collections
from operator import truediv
from tkinter.tix import ListNoteBook
from typing import Deque, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head: ListNode) -> None: 
  nodes = []
  while head:
    nodes.append(head.val)
    head = head.mnext

  while nodes:
    print(nodes.pop())

'''
8.1 Max Stack Library
'''

class Stack:
  ElementWithCatchedMax = collections.namedTuple('ElementWithCachedMax', ('element', 'max'))

  def __init__(self) -> None:
    self._element_with_cached_max: List[Stack.ElementWithCatchedMax] = []

  def empty(self) -> bool:
    return len(self._element_with_cached_max) == 0

  def max(self) -> int:
    return self._element_with_cached_max[-1].max

  def pop(self) -> int:
    return self._element_with_cached_max.pop().element

  def push(self, x: int) -> None:
    self._element_with_cached_max(self.ElementWithCatchedMax(
      x, x if self.empty() else max(x, self.max())
    ))  

'''
8.2 Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression
would always evaluate to a result, and there will not be any division by zero operation.
'''
def evalRPN(self, tokens: List[str]) -> int:
    operators = {
        '+': lambda y, x : x + y,
        '-': lambda y, x : x - y,
        '*': lambda y, x : x * y,
        '/': lambda y, x : int(truediv(x,y))
    }
    
    stack = []
    for i in tokens:
        if i in operators:
            stack.append(operators[i](stack.pop(), stack.pop()))
        else:
            stack.append(int(i))
            
    return stack[-1]

'''
8.3 Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
def isValid(self, s: str) -> bool:
  if len(s) % 2 != 0:
      return False
  
  opened = ["(","{","["]
  closed = [")","}","]"]
  
  stack = []
  for i in s:
      if i in opened:
          stack.append(i)
      elif i in closed:
          pos = closed.index(i)
          
          if len(stack) > 0 and opened[pos] == stack[-1]:
              stack.pop()
          else:
              return False

  return True if len(stack) == 0 else False

def isValid(self, s: str) -> bool:       
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('{}','').replace('()','').replace('[]','')
    
    return True if s == '' else False


'''
8.4 shortest Pathname

Given a string path, which is an absolute path (starting with a slash '/') to a file or
 directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double
 period '..' refers to the directory up a level, and any multiple consecutive slashes 
 (i.e. '//') are treated as a single slash '/'. For this problem, any other format 
 of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from 
the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
'''

def simplifyPath(self, path: str) -> str:
    stack = []
    curr = ""
    
    for c in path +'/':
        if c == '/':
            if curr == '..':
                if stack: stack.pop()
            elif curr != "" and curr != '.':
                stack.append(curr)
            curr = ""
        else:
            curr += c
            
    return '/' + '/'.join(stack)


'''Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is 
being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets 
are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and 
that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.'''

def decodeString(self, s: str) -> str:
    stack = []
    
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            word = ""
            while stack[-1] != '[':
                word = stack.pop() + word
            stack.pop()
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
                
            stack.append(int(k) * word)
    
    return "".join(stack)



'''Queues Bootcamp'''

class Queue:
  def __init__(self) -> None:
    self._data: Deque[int] = collections.deque()
    
  def enqueue(self, x: int) -> None:
    self._data.append(x)

  def dequeue(self) -> int:
    return self._data.popleft()
  
  def max(self) -> int:
    return max(self._data)

'''
8.6 Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its 
nodes' values. (i.e., from left to right, level by level).
'''
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = collections.deque()
    q.append(root)
    
    while q:
        qlen = len(q)
        level = []
        for i in range(qlen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
                
        if level:
            res.append(level)
            
    return res


'''
8.8 Implement a queue using stacks
Queue insertion and deletion follows first-in, first-out semantics; stack inseration and deletion is last in, first-out
How would you implement a queue given a library implementing stacks?
'''

class Queue:
  def __init__(self) -> None:
    self._enq: List[int] = []
    self._deq: List[int] = []

  def enqueue(self, x: int) -> None:
    self._enq.append(x)

  def dequeue(self) -> int:
    if not self._deq:
      # Transfers the elements in _enq to _deq
      while self._enq:
        self._deq.append(self._enq.pop())
    return self._deq.pop()



'''
 Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k 
adjacent and equal letters from s and removing them, causing the left and the right side of 
the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. 
It is guaranteed that the answer is unique.'''

def removeDuplicates(self, s: str, k: int) -> str:
  stack = [] #char, count 
  
  for c in s:
      if stack and stack[-1][0] == c:
          stack[-1][1] +=1 
      else:
          stack.append([c,1])
      
      if stack[-1][1] == k:
          stack.pop()
          
  res = ""
  for char, count in stack:
      res += (char * count)
      
  return res


'''
Generate Paranthesis

Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.

'''
def generateParenthesis(self, n: int) -> List[str]:
    
    stack = []
    res = []
    
    def backtrack(openN, closedN):
        
        if len(stack) == 2 *n:
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            backtrack(openN+1, closedN)
            stack.pop()
            
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN+1)
            stack.pop()
            
    backtrack(0,0)
    return res