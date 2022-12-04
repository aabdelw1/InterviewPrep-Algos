#Chapter 16 Problems: 1,2,3,6; 5,7,12
#Completed: 1,2,

'''Dynamic Programming Bootcamp'''

'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,'''

#Recursively
def fib(self, n: int) -> int:
    
    if n <= 1:
        return n
    
    return self.fib(n-1) + self.fib(n-2)

#Dynamically
def fib(self, n: int) -> int:
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1,n):
      f = f_minus_1 + f_minus_2

      f_minus_2 = f_minus_1
      f_minus_1 = f

    return f_minus_1

'''
Maximum Subarray

Given an integer array nums, find the subarray which has the largest sum and return its sum.
'''

#brute force
def maxSubArray(self, nums: List[int]) -> int:
  max_subarray = -math.inf
  for i in range(len(nums)):
      current_subarray = 0
      for j in range(i, len(nums)):
          current_subarray += nums[j]
          max_subarray = max(max_subarray, current_subarray)
  
  return max_subarray


#Dynamically
def maxSubArray(self, nums: List[int]) -> int:
    max_seen = max_end = float('-inf')
    
    for i in nums:
        max_end = max(i, i + max_end)
        max_seen = max(max_end, max_seen)
        
    return max_seen



'''
16.1 Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list 
of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations 
are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.'''

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
    res = []
    
    def dfs(i, cur, total):
        
        if total == target:
            res.append(cur.copy())
            return
        
        if i >= len(candidates) or total > target:
            return
        
        cur.append(candidates[i])
        dfs(i, cur, candidates[i] + total)
        cur.pop()
        dfs(i+1, cur, total)
        
    dfs(0,[],0)
    return res


'''
16.1.1 Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
                
    print(dp)
                
    return dp[0][0]


'''
16.2 Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
'''

def minDistance(self, word1: str, word2: str) -> int:        
    dp = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) +1)] 
    
    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j
        
    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i
        
    for i in range(len(word1)-1, -1, -1):
        for j in range(len(word2)-1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
                
            else:
                dp[i][j] = 1 + min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
                
    return dp[0][0]


'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

'''

def trap(self, height: List[int]) -> int:
    
    maxLeft = [0] * (len(height)+2)
    maxRight = [0] * (len(height)+2)
    minLR = [0] *  (len(height)+2)
    
    area = 0
    for i in range(len(height)-1,0,-1):
        maxRight[i-1] = max(maxRight[i], height[i])
    
    for i in range(0, len(height)):
        maxLeft[i] = max(maxLeft[i-1], height[i])
        minLR[i] = min(maxLeft[i], maxRight[i])
        
    for i in range(len(height)):
        if minLR[i] - height[i] >= 0:
            area += minLR[i] - height[i]
            
    return area

def trap(self, height: List[int]) -> int:
    
    if not height: return 0
    
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[0], height[-1] 
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
            
    return res