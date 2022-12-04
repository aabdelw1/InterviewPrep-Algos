#Chapter 10 Problems: 1,4,3,5,6
#Completed: 1,4,3,5

'''Heaps Bootcamp'''

'''
- A heap is a specialized binary tree
- Heap property: the key at each node is at least as great as the keys stared at its children
- A max heap can be implemented as array: children of each node at index i are (2i+1 and 2i+2)
- Referred to as a priortiy queue with the difference that each element has a priority associated
  with it and deletion removes the element with the highest prioirty

- Use a heap when all you care about is the smallest or largest elementsi in an array
  - do not need fast look up, delete, search operations for arbitrary elements
  - k largest: min-heap
  - k smallest: max-heap

- to make a maxheap, insert coreesponding negative values into 
'''

import heapq
import itertools
import math
from typing import Iterator, List

def lib():
  heapq.heapify(L) #Transforms the elements in L into a heap in place
  heapq.nlargest(k, L) #returns the kths largest in L
  heapq.nsmallest(k, L) #returns the kths smallest in L
  heapq.heappush(L, e) #pushes a new element onto the heap
  heapq.heappop(L) #removes the smallest element from the heap
  heapq.heappushpop(L, a) #pushes a into the heap and removes smallest element
  e = L[0] #returns smallest element in the heap
'''
Heaps Library
'''



'''
10.0 Kth largest element in a Stream

Design a class to find the kth largest element in a stream. Note that 
it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''
class KthLargest:
  def __init__(self, k: int, nums: List[int]):
      
      self.minHeap = nums
      self.k = k
      heapq.heapify(self.minHeap)
      
      while len(self.minHeap) > k:
          heapq.heappop(self.minHeap)

  def add(self, val: int) -> int:
      
      heapq.heappush(self.minHeap, val)
      if len(self.minHeap) > self.k:
          heapq.heappop(self.minHeap)
      
      return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


'''
10.1 Merge two sorted arrays

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
 integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
 inside the array nums1. To accommodate this, nums1 has a length of m + n, where the 
 first m elements denote the elements that should be merged, and the last n elements 
 are set to 0 and should be ignored. nums2 has a length of n.
'''
#using heap
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    total_length, heap = len(nums1), list()
    for i in range(m):
        heapq.heappush(heap, nums1[i])
    for i in range(n):
        heapq.heappush(heap, nums2[i])        
        
    for i in range(total_length):
        nums1[i] = heapq.heappop(heap) 
        
    return nums1

#not using heap
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  end = m + n - 1
  
  while m > 0 and n > 0:
      if nums1[m-1] > nums2[n-1]:
          nums1[end] = nums1[m-1]
          m -=1
      else:
          nums1[end] = nums2[n-1]
          n -=1
      end -= 1
      
  while n > 0:
      nums1[end] = nums2[n-1]
      n -=1
      end-=1
  return nums1


'''
10.4 K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the
 X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

'''
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
    minClosest = []
    heapq.heapify(minClosest)
    o = [0,0]
    
    for i in points: 
        dis = math.dist(o,i)
        heapq.heappush(minClosest, (-dis, i))
      
    while len(minClosest) > k:
        heapq.heappop(minClosest)
        
    return [s[1] for s in minClosest]

  
'''
10.3 Sort an almost sorted array

Write a program which takes as input a very long sequence of numbers and prints the numbers in sorted order.
Each number is at most k away from its correctly sorted position. Such an array is somtimes referred to as being k sorted
'''
def sort_almost_sorted_array(sequence: Iterator[int], k:int) -> List[int]:
  minHeap = List()
  for x in itertools.islice(sequence, k):
    heapq.heappush(minHeap, x)

  result = []
  for x in sequence:
    smallest = heapq.heappushpop(minHeap, x)
    result.append(smallest)

  while minHeap:
    smallest = heapq.heappop(minHeap)
    result.append(smallest)
  
  return result

'''
10.5 Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of
the actual answer will be accepted.
'''

class MedianFinder:
  def __init__(self):
      self.small = []
      self.large = []
      
  def addNum(self, num: int) -> None:
      heapq.heappush(self.small, num * -1)
      
      #uneven order
      if (self.small and self.large and 
              -1* self.small[0] > self.large[0]):
          val = -1 * heapq.heappop(self.small)
          heapq.heappush(self.large, val)
          
      #uneven size   
      if len(self.small) > len(self.large) + 1:
          val = -1 * heapq.heappop(self.small)
          heapq.heappush(self.large, val)
          
      if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val*-1)
      
  def findMedian(self) -> float:
      if len(self.small) > len(self.large):
          return self.small[0] * -1
      
      if len(self.large) > len(self.small):
          return self.large[0]
      
      return (-1* self.small[0] + self.large[0]) / 2



'''
10.6 Compute the k largest elemnts in a max-heap

A heap contains limited information about the ordering of elements, so unlike a sorted array or a
balanced BST, naive algorithms for computing the k largest elements have a time complexity that 
depends linearly on the number or elements in that collection

Given a max heap as an array, implement List<Integer> peekTopK(int[] arr, int k) to find the top k 
elements. Do not modify the heap or copy entire heap to a different data structure. Example:
'''

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
  if k <= 0:
    return []

  # Stores the (-value, index) pair in candidate_max_heap. This heap is
  # ordered by value field. Uses the negative of value to the get the 
  # effect of a max-heap
  
  candidate_max_heap = []
  # Largest elemennt in A is at index 0
  candidate_max_heap.append((-A[0], 0))
  result  = []

  for _ in range(k):
    print(candidate_max_heap)
    candidate_index = candidate_max_heap[0][1]
    result.append((-heapq.heappop(candidate_max_heap)[0]))

    left_child_i = 2 * candidate_index + 1
    if left_child_i < len(A):
      heapq.heappush(candidate_max_heap, (-A[left_child_i], left_child_i))

    right_child_i = 2 * candidate_index + 2
    if right_child_i < len(A):
      heapq.heappush(candidate_max_heap, (-A[right_child_i], right_child_i))

  return result


print(k_largest_in_binary_heap([561,314,401,28,156,359,271,11,3], 4))



