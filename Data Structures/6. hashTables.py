#Chapter 12 Problems: 2,3,5; 1,4,6,9
#Completed: 1,2,3,5,6

'''Hash Tables Bootcamp

A hash table is a data structure used to store keys, optionally, with corresponding values.
Inserts, deletes and lookups run in O(1) time on average.
'''

'''
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

import collections
from typing import Dict, List
import typing
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    sorteds = collections.defaultdict(list)
    for s in strs:
        sorteds[''.join(sorted(s))].append(s)
        
    return [group for group in sorteds.values()]


'''
12.1 Test for palindromic permutations

Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.
'''
def canPermutePalindrome(self, s: str) -> bool:
    d = collections.defaultdict(list)
    
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    counter = 0
    for key in d.values():
        counter += key % 2
        
    return counter <= 1

'''
12.2 Ransome Note 

Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.'''

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    return not collections.Counter(ransomNote) - collections.Counter(magazine)

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
  char_frequency = collections.Counter(ransomNote)

  for c in magazine:
      if c in char_frequency:
          char_frequency[c] -= 1
          if char_frequency[c] == 0:
              del char_frequency[c]

          if not char_frequency:
              return True
      
  return not char_frequency 

'''
12.3 LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
 evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

class LRUCache:
  def __init__(self, capacity: int):
      self.lru = collections.defaultdict(list)
      self.capacity = capacity

  def get(self, key: int) -> int:
      
      if key not in self.lru:
          return -1
      else:
          return self.updateOrder(key)

  def put(self, key: int, value: int) -> None:
      
      if key not in self.lru:
          if len(self.lru) >= self.capacity:
              self.lru.pop(next(iter(self.lru)))
          self.lru[key] = value
          
      else:
          self.updateOrder(key)
          self.lru.update({key:value})
          
  def updateOrder(self, key: int) -> None:
      val = self.lru[key]
      del self.lru[key]
      self.lru[key] = val
      return val

#Book solution
class LRUCache:
    def __init__(self, capacity):
      self.dic = collections.OrderedDict()
      self.remain = capacity

    def get(self, key):
      if key not in self.dic:
          return -1
      v = self.dic.pop(key) 
      self.dic[key] = v   # set key as the newest one
      return v

    def set(self, key, value):
      if key in self.dic:    
          self.dic.pop(key)
      else:
          if self.remain > 0:
              self.remain -= 1  
          else:  # self.dic is full
              self.dic.popitem(last=False) 
      self.dic[key] = value
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
'''

def findDuplicates(self, nums: List[int]) -> List[int]:
  dic = {}
  
  for i in nums:
      if i in dic:
          dic[i] += 1
      else:
          dic[i] = 1
          
  return [key for key, value in dic.items() if value > 1]

'''
12.5 Find the nearest repeated entries in an array

Write a program which takes as input an array and finds the distance between a closet pair of equal entries.
For example if s = ['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results']
then the second and third occurances of "no" is the closet pair
'''

def find_nearest_repetition(paragraph: List[str]) -> int:
  word_to_last_index: Dict[str, int] = {}

  nearest_repeated_distance = float('inf')
  for i, word in enumerate(paragraph):
    if word in word_to_last_index:
      latest_equal_world = word_to_last_index[word]
      nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_world)

    word_to_last_index[word] = i
  return typing.cast(int, nearest_repeated_distance) if nearest_repeated_distance != float('inf') else -1

# find_nearest_repetition(['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results'])

'''
12.6 Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring 
of s such that every character in t (including duplicates) is included in the window.
 If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.'''

def minWindow(self, s: str, t: str) -> str:
    
    if t == "": return ""
    
    window = {}
    countT = Counter(t)
            
    have = 0
    need = len(countT)
    res, resLen = [-1, -1], float('infinity')
    l = 0
    for r in range(len(s)):
        c = s[r]
        
        window[c] = 1 + window.get(c, 0)
        
        if c in countT and window[c] == countT[c]:
            have += 1
            
        while have == need:
            #update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            #pop from the left from our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if resLen != float('infinity') else ""



'''12.9 Longest Consecutive Interval

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''


def longestConsecutive(self, nums: List[int]) -> int:

  numsSet = set(nums)                
  longest = 0

  for num in nums:
      if (num - 1) not in numsSet:
          length = 1 
          while (num + length) in numsSet:
              length += 1
          longest = max(longest, length)
              
  return longest