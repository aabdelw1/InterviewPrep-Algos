#Chapter 5 Problems: 1,6,12,18,2,17,5,9,3,10,15
#Completed: 1,2,3,4,5,6,7,12,18,17,9

'''Arrays Bootcamp'''

from typing import List
import random
import collections

'''
0. Your input is an array of integers, and you have to reorder its entreis to that the even 
entries appear first. This is easy if you use O(n) space, where n is the length of the 
array. However, you are required to solve it without allocating additional storage'''

def even_odd(A: List[int]) -> None:
  next_even, next_odd = 0, len(A) - 1
  while next_even < next_odd:
    if A[next_even] % 2 == 0:
      next_even += 1
    else:
      A[next_even], A[next_odd] = A[next_odd], A[next_even]
      next_odd -= 1
  return A
# print(even_odd([1,4,3,6,7,2,6]))

''' 
1. Write a program that takes an array A and an index i into A, and rearranges the elements
such that all elements less than A[i] appear first, followed by lelements equal to the
pivot, followed by elements greater than the pivot '''

#O(n^2)
def dutch_flag_partiion(pivot_index: int, A: List[int]) -> None:
  pivot = A[pivot_index]
  #first pass, group elements smaller than pivot
  for i in range(len(A)):
    #Look for a smaller element
    for j in range(i+1, len(A)):
      if A[j] < pivot:
        A[i], A[j] = A[j], A[i]
        break

  #second pass, group elements larger than the pivot
  for i in reversed(range(len(A))):
    #Look for a larger element. Stop when we reach an element less than
    #pivot, since first pass has moved them to the start of A
    for j in reversed(range(i)):
      if A[j] > pivot:
        A[i], A[j] = A[j], A[i]
        break
  return A
# print(dutch_flag_partiion(3,[0,1,2,0,2,1,1]))

#O(n)
def dutch_flag_partiion2(pivot_index: int, A: List[int]) -> None:
  pivot = A[pivot_index]
  #First pass: group elements smaller than pivot
  smaller = 0
  for i in range(len(A)):
    if A[i] < pivot:
      A[i], A[smaller] = A[smaller], A[i]
      smaller += 1
  
  #Second pass: group elements larger than pivot
  larger = len(A) - 1
  for i in reversed(range(len(A))):
    if A[i] > pivot:
      A[i], A[larger] = A[larger], A[i]
      larger -= 1
  return A
# print(dutch_flag_partiion2(3,[0,1,2,0,2,1,1]))

def dutch_flag_partiion3(pivot_index: int, A: List[int]) -> None:
  pivot = A[pivot_index]
  smaller, equal, larger = 0,0, len(A)

  while equal < larger:
    if A[equal] < pivot:
      A[smaller], A[equal] = A[equal], A[smaller]
      smaller, equal = smaller + 1, equal + 1

    elif pivot == A[equal]:
      equal += 1
    else: #  A[equal] > pivot:
      larger -= 1

      A[equal], A[larger] = A[larger], A[equal]

  return A
# print(dutch_flag_partiion3(3,[0,1,2,0,2,1,1]))


'''
3. You are given a large integer represented as an integer array digits, where each digits[i] is the 
ith digit of the integer. The digits are ordered from most significant to least significant in 
left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.'''

def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits)-1, -1, -1):
        digits[i] += 1
        if digits[i] != 10:
            return digits
        
        digits[i] = 0
        
    return [1] + digits
# print(plusOne([9]))

'''
4. Given two integers num1 and num2 represented as lists, return the product of num1 and num2,
also represented as a list. num1 and num2 maybe negative if the leading digit is negative.'''


def multiple(nums1: List[int], nums2: List[int]) -> List[int]:
  
  sign = -1 if nums1[0] * nums2[0] < 0 else 1

  nums1[0], nums2[0] = abs(nums1[0]), abs(nums2[0])
  result = [0] * (len(nums1) + len(nums2))
  for i in range(len(nums1)-1,-1,-1):
    for j in range(len(nums2)-1, -1, -1):
      result[i+j+1] += nums1[i] * nums2[j]
      result[i+j] += result[i+j+1] // 10
      result[i+j+1] %= 10

  while result[0] == 0:
    result.pop(0)

  result[0] *= sign
  return result

# print(multiple([1,0,3,5,2], [-1,0]))

'''
5. You are given an integer array nums. You are initially positioned at the array's first 
index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.'''

def canJump(self, nums: List[int]) -> bool:
  last_index = len(nums) -1
  furthest_distance_possible = 0
  i = 0
  while i <= furthest_distance_possible and furthest_distance_possible < last_index:
      furthest_distance_possible = max(furthest_distance_possible, nums[i] + i) 
      i += 1

  return furthest_distance_possible >= last_index



'''
6. remove duplicates from a sorted array'''
def removeDuplicates(self, nums: List[int]) -> int:  
    if not nums:
        return 0

    newTail = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[newTail]:
            newTail += 1
            nums[newTail] = nums[i]

    return newTail + 1

def removeDuplicates(self, nums: List[int]) -> int:
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l


'''
7. You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

#O(n) time O(1) space
def maxProfit(self, prices: List[int]) -> int:
  
    min_price_so_far = float('inf')
    max_profit = 0
    for price in prices:
        max_profit_so_far = price - min_price_so_far
        min_price_so_far = min(price, min_price_so_far)
        max_profit = max(max_profit, max_profit_so_far)  
    return max_profit


'''
12. Given an array A of n elements and a number 0<=k<=n, return a subset of A of size k.

Input: A = [5, 11, 3, 7], k =3
Output: [3, 7, 11]
Note that there is no fixed output. It might vary for each run.
'''

#O(k) time and O(1) space
def random_sampling(k: int, A: List[int]) -> List[int]:
  for i in range(k):
    #generate random number from i to length of A
    j = random.randint(i, len(A)-1)
    A[i], A[j] = A[j], A[i]
  return A[:k]

# print(random_sampling(3, [5, 11, 3, 7]))


'''
18. Given an m x n matrix, return all elements of the matrix in spiral order'''
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    spiral = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    while left < right and top < bottom:
        #get every element in the top row
        for i in range(left, right):
            spiral.append(matrix[top][i])
        top +=1
      
        #get every element from right most colomn
        for i in range(top, bottom):
            spiral.append(matrix[i][right-1])
        right -=1
        
        if not (left < right and top < bottom):
            break
        
        for i in range(right-1, left-1, -1):
            spiral.append(matrix[bottom-1][i])
        bottom -= 1
        
        for i in range(bottom-1, top-1, -1):
            spiral.append(matrix[i][left])
        left += 1
        
    return spiral


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:      
    return matrix and list(matrix.pop(0)) + self.spiralOrder([*zip(*matrix)][::-1])
    

'''
17. Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.'''
def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
                
            if(board[r][c] in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in squares[(r//3, c//3)]):
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    
    return True

'''
19. Given an integer n, return the number of prime numbers that are strictly less than n.'''

def countPrimes(self, n: int) -> int:
    if n == 0 or n == 1:
        return 0
    
    #sieve of eratothenese
    primes = [0,0] + [1] * n
    i = 2
    while i * i < n:
        tmp = i
        if primes[i]:
            tmp+= i
            while tmp < n:
                primes[tmp] = 0
                tmp += i
        i+=1
        
    return sum(primes)

def countPrimes(n: int) -> List[int]:
  primes = []
  # is_prime[p] represents if p is prime or not, Initially, set ot true
  # true, expecting 0 and 1. Then use sieving to elimate nonprimes
  is_prime = [0,0] + [1] * (n-1)
  for p in range(2, n+1):
    if is_prime[p]:
      primes.append(p)
      for i in range(p*2, n+1, p):
        is_prime[i] = 0

  return primes

'''
10. Permutate the elements of an array '''

def apply_permutation(perm: List[int], A: List[int]) -> None:
  for i in range(len(A)):
    while perm[i] != i:
      A[perm[i]], A[i] = A[i], [perm[i]]
      perm[A[i]], perm[i] = perm[i], [A[i]]


'''
Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b
'''
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    
    l, r = 0, len(arr) - k
    
    while l < r:
        m = (l + r) // 2
        if x - arr[m] > arr[m+k] - x:
            l = m + 1
        else:
            r = m
    return arr[l:l+k]


'''
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
 that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    
    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            curSum = nums[i] + nums[l] + nums[r] 
            
            if curSum == 0:
                res.append([nums[i],nums[l],nums[r]])
                l+= 1
                while l < r and nums[l] == nums[l-1]:
                    l+= 1
                    
            elif curSum > 0:
                r = r - 1
            else:
                l = l + 1
                
    return res