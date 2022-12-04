#Chapter 13 Problems: 1,2,6; 8,11,9
#Completed: 1,2,6


'''Sorting Bootcamp'''

import collections


class Student:
  def __init__(self, name: str, grade_point_average: float) -> None:
    self.name = name
    self.grade_point_average = grade_point_average


  def __lt__(self, other: 'Student') -> bool:
    return self.name < other.name

students = [
  Student('A', 4.0),
  Student('C', 3.0),
  Student('B', 2.0),
  Student('D', 3.2)
]

# Sort according to __lt__ defined in Student. students remained unchanged
students_sort_by_name = sorted(students)

# Sort students in-place by grade_point_average
students.sort(key=lambda student: student.grade_point_average)

'''
13.1 Intersection of two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
'''

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
  i, j, inter = 0,0, [] 
  nums1.sort()
  nums2.sort()

  while i < len(nums1) and j < len(nums2):
      if nums1[i] == nums2[j]:
          if i == 0 or nums1[i] != nums1[i-1]:
              inter.append(nums1[i])
          i += 1
          j += 1

      elif nums1[i] < nums2[j]:
          i += 1
      else:
          j += 1

  return inter

#hash map
#Time and Space complexity: O(m + n) = O(max(m, n))
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap = {}
    res = set()
    
    for i in range(len(nums1)):
        hashmap[nums1[i]] = i
    
    for n in nums2:
        if n in hashmap:
            res.add(n)
            
    return res


'''
13.2 Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the 
array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote 
the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''


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
        
    return nums

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    left = 0
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
13.6.1 Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''

def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    
    intervals.sort()
    
    prevEnd = intervals[0][1]
    res = 0 
    
    for start, end in intervals[1:]:
        print(start, end)
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(prevEnd, end)
            
    return res


'''
13.6.2 Meeting Rooms ii

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.
'''

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    
    res, count = 0, 0
    s, e = 0, 0
    
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1 
            count += 1
        else:
            e += 1
            count -= 1
            
        res = max(count,res)
        
    return res

'''
13.6 Render a Calendar

Write a program that takes a set of events, and determines the maximum number of events that take place concurrently
Focus on endpoints
'''

Event = collections.namedTuple('Event', ('start', 'finish'))

def find_max_simulataneous_events(A: List[Event]) -> int:
  Endpoint = collections.namedtuple('EndPoint', ('time', 'is_start'))
  E = [ p for event in A for p in (Endpoint(event.start, True), Endpoint(event.finish, False))]
  E.sort(key=lambda e: (e.time, not e.is_start))
  max_num_simultaneous_events, num_simultaneous_events = 0, 0
  for e in E:
    if e.is_start:
      num_simultaneous_events += 1
      max_num_simultaneous_events = max(num_simultaneous_events, max_num_simultaneous_events)

    else:
      num_simultaneous_events -= 1

  return max_num_simultaneous_events


'''
13.4 H-index

Given an array of integers citations where citations[i] is the number of citations a researcher received for 
their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n 
papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index'''

def hIndex(self, citations: List[int]) -> int:
    
    citations.sort()
    dic = {}
    h = 0
    for index, val in enumerate(citations):
        if val >= len(citations)-index:
            return len(citations)-index
        
        
    return 0