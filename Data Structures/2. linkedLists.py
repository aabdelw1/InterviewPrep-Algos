#Chapter 7 Problems: 1,2,3,4,7,10,11
#Completed: 1,2,3,4,7,10,11

'''Linked Lists Bootcamp'''

from tkinter.tix import ListNoteBook
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def search_list(L: ListNode, key: int) -> ListNode:
  while L and L.data != key:
    L = L.next
  return L

#insert new node after a specific node
def insert_after(node: ListNode, new_node: ListNodse) -> None:
  new_node.next = node.next
  node.next = new_node

#delete the new past this one
def delete_after(node: ListNode) -> None:
  node.next = node.next.next


'''
7.1 
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
'''

def mergeTwoLists(self, list1: Optional[ListNoteBook], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next  
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 or list2
    
    return dummy.next

'''
Reverse Linked List I
Given the head of a singly linked list, reverse the list, and return the reversed list.'''

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
          
    return prev

'''
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    
    carry = 0
    
    while l1 or l2:
        var1 = l1.val if l1 else 0
        var2 = l2.val if l2 else 0
        
        #new digiit
        val = var1 + var2 + carry
        carry  = val // 10
        val = val % 10
        curr.next = ListNode(val)
        
        #update pairs
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next


'''
7.2 Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
'''

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
  dummy = ListNode(0, head)
  leftPrev = dummy
  cur = head
  
  # 1) reach node at position left
  for i in range(left - 1):
      leftPrev = cur
      cur = cur.next
      
  # Now cur = "left", leftPrev = "node before"
  # 2) reverse from left to right
  prev = None
  for i in range(right - left + 1):
      tempNext = cur.next
      cur.next = prev
      prev = cur
      cur = tempNext
      
  #3) Update pointers
  leftPrev.next.next = cur
  leftPrev.next = prev
  
  return dummy.next

'''
7.3 Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed
as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
'''
#time: O(n), space: O(n)
def hasCycle(self, head: Optional[ListNode]) -> bool:
    
  hashSet = {}
  while head:
      if head in hashSet:
          return True
      else:
          hashSet[head] = True  
      head = head.next
  return False
    
#time: O(n), space: O(1)
def hasCycle(self, head: Optional[ListNode]) -> bool:
  slow, fast = head, head
  
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      
      if slow == fast:
          return True
      
  return False


'''
7.4 Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.'''
#time: O(n + m), space: O(n)
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    hashSet = {}
    
    while headA:
        hashSet[headA] = True
        headA = headA.next
        
    while headB:
        if headB in hashSet:
            return headB
        headB = headB.next
        
    return None

#time: O(n + m), space: O(1)
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
  l1, l2 = headA, headB

  while l1 != l2:
      l1 = l1.next if l1 else headB
      l2 = l2.next if l2 else headA
      
  return l1


'''
7.7 Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head. '''

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  dummy = ListNode(0, head)
  left = dummy
  right = head
    
  while n > 0 and right:
        right = right.next
        n-= 1
        
  while right:
    left = left.next
    right = right.next

  left.next = left.next.next
    
  return dummy.next

#worse solutuion
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  if head.next == None:
      return None
  tmp = head
  size = 0

  # find the size of the linked list
  while tmp:
      size += 1
      tmp = tmp.next
  tmp = head

  #if we have to remove the first node:
  if n == size: 
      return head.next

  for _ in range(size-n-1):
      tmp = tmp.next
  tmp.next = tmp.next.next
  return head

'''
7.10 Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed
by the nodes with even indices, and return the reordered list. The first node is considered odd, 
and the second node is even, and so on. Note that the relative order inside both the even and 
odd groups should remain as it was in the input. You must solve the problem in O(1) extra space 
complexity and O(n) time complexity.

'''
def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head
    
    odd = head # Both of them point at the first node of the target linked list
    even = head.next # doesn't matter even there's only one node in the linked list (even will become None)
    eHead = even # We have to keep where the even-node list starts
    
    while even and even.next: # won't get in the loop at first if there's only one node in the linked list
        # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
        # AND, why these two, small discussion by myself as below
        odd.next = odd.next.next
        even.next = even.next.next
        # After these two ops, odd/even still points at its original place
        # Therefore, we move them to the next node repectively
        odd = odd.next
        even = even.next
    
    odd.next = eHead # the odd pointer currently points at the last node of the odd-node list
    
    return head # We keep the start of the odd-node list in the first of our code


'''
7.11 Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.'''

#O(n) time and O(1) space
def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        #find middle (slow)
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        prev = None
        #reverse second half
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow 
            slow = tmp
            
        #check palindrome
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

#O(n) time and O(n) space
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    nums = []
    
    while head:
        nums.append(head.val)
        head = head.next
        
    l, r = 0, len(nums) - 1
        
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True


