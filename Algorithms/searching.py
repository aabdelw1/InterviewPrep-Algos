#Chapter 11 Problems: 1,4,8,3,9,5,10,6,7
#Completed: 1,4,8,3


'''Searching Bootcamp'''

'''
Binary Search can be written in many way-recursive, iterative, differnt idioms for conditionals, etc
Here is an iterative implementation adapted from Bentley's book, which includes the bug
'''

import bisect
import collections
import heapq
from typing import Callable, List, Tuple


def bsearch(t: int, A: List[int]) -> int:
  L, U = 0, len(A) - 1

  while L <= U:
    M = L + U //2
    # M = L + (U - L) /2
    if A[M] < t:
      L = M + 1
    elif A[M] == t:
      return M
    else: 
      U = M - 1

  return -1

'''
Suppose we are given as input an array of students, sorted by descending GPA, with ties broken on name. 
In the program below, we show how to use the library binary search routine to perform fast searches
in this array. In particular, we pass binary search a custom comparator which compares students
on GPA (higher GPA comes first), with ties broken on name.'''

Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa (student: Student) -> Tuple[float, str]:
  return (-student.grade_point_average, student.name)

def search_student(students: List[Student], target: Student, comp_gpa: Callable[[Student], Tuple[float, str]]):
  i = bisect.bisect_left ([comp_gpa(s) for s in students], comp_gpa(target))
  return 0 <= i < len(students) and students [i] == target


'''
11.1 Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.'''

# brute force inefficent O(n)
def searchRange(self, nums: List[int], target: int) -> List[int]:
    if target not in nums:
      return [-1,-1]
    res = []
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)
            break
        
    for i in range(len(nums)-1, -1, -1):
          if nums[i] == target:
            res.append(i)
            break
            
    return res

# efficient with libraries O(log n)
def searchRange(self, nums: List[int], target: int) -> List[int]:
    
    if target not in nums:
        return [-1,-1]
    
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target) - 1

    return [left, right]

# efficient without libraries O(log n)
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
      
      left = self.binarySearch(target, nums, True)
      right = self.binarySearch(target, nums, False)
      
      return [left, right]
      
  def binarySearch(self, target, nums, leftBias):
      l, r = 0, len(nums) - 1
      i = -1
      while l <= r:
          m = (l+r) //2
          if nums[m] < target:
              l = m + 1
          elif nums[m] > target:
              r = m - 1
          else:
              i = m
              if leftBias:
                  r = m - 1
              else:
                  l = m + 1

      return i 


'''
11.4 Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to 
the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.'''

def mySqrt(self, x: int) -> int:
  left, right = 0, x
  
  while left <= right:
      mid = (left + right) // 2
      square = mid * mid
      if square <= x:
          left = mid + 1
      else:
          right = mid - 1
            
  return left - 1

 
'''
11.8 Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.'''

def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort()
    return nums[(len(nums) - k)]

def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)
        
    return nums[0]

def findKthLargest(self, nums: List[int], k: int) -> int:
    k = len(nums) - k
    
    def quickselect(l, r):
        pivot, p = nums[r], l
        
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        
        if p > k: return quickselect(l, p - 1)
        elif p < k: return quickselect(p + 1, r)
        else: return nums[p]
                
    return quickselect(0, len(nums) - 1)

'''
11.3 Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
 in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.'''

def findMin(self, nums: List[int]) -> int:

    heapq.heapify(nums)
    return heapq.heappop(nums)

def findMin(self, nums: List[int]) -> int:

  left, right = 0, len(nums) -1
  
  while left < right:
      mid = (left + right) // 2
      
      if nums[mid] > nums[right]:
          left = mid + 1
      else:
          right = mid
  return nums[left]



'''
11.3.1 Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index 
k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated
at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.'''

def search(self, nums: List[int], target: int) -> int:
    
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1