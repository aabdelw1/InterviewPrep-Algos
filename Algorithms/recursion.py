#Chapter 15 Problems: 1,3,4; 5,10,7,11
#Completed: 1,2,3,4

'''Recursion Bootcamp'''

'''
GCD is a great example of recursion
'''

def gcd(x: int, y: int) -> int:
  return x if y == 0 else gcd(y, x%y) 



'''
15.1 Tower of Hanoi

Tower of Hanoi is a mathematical puzzle where we have 3 rods and n disks. 
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
- Only one disk can be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of 
  another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
- No disk may be placed on top of a smaller disk.

Write a program which prints a sequence of operations that move n disks from one rod to another.

'''

def tower_of_hanoi(n):
    # Recursive function to solve tower of hanoi   
    def helper(n , from_rod, to_rod, aux_rod): 
        # this recursion covers base cases

        # move top n-1 disks to aux_rod
        helper(n-1, from_rod, aux_rod, to_rod) 
        # move the nth disk to to_rod
        print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
        # move top n-1 disks to to_rod
        helper(n-1, aux_rod, to_rod, from_rod) 

    helper(n, 'A', 'B', 'C')  
    # A, C, B are the name of rods


'''
15.2 Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
 combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.'''


def letterCombinations(self, digits: str) -> List[str]:
    res = []
    letters = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv',                     '9':'wxyz'}

    def helper(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for c in letters[digits[i]]:
            helper(i+1, curStr + c)
    
    
    if digits:
        helper(0, "")
        
    return res


'''
15.3 Solve N Queens

The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.'''

def solveNQueens(self, n: int) -> List[List[str]]:
    cols = set()
    posDiag = set() #(r+c)
    negDiag = set() #(r-c)
    
    res = []
    board = [['.'] * n for i in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = [("").join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                continue
            
            cols.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"
                
            backtrack(r + 1)
            
            cols.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."
            
    backtrack(0)
    return res
    
def solveNQueens(self, n: int) -> List[List[str]]:
    
    def backTrack(row):
        if row == n:
            result.append(col_placement.copy())
            return
        
        for col in range(n):
            if all(abs(c-col) not in (0, row-i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
        backTrack(row + 1)
            
    result = []
    col_placement = [0] * n
    backTrack(0)
    return result


'''
15.4 Permutations 

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

'''

def permute(self, nums: List[int]) -> List[List[int]]:
    
    result = []
    
    if len(nums) == 1: 
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        
        perms = self.permute(nums)
        
        for perm in perms:
            perm.append(n)
            
        result.extend(perms)
        nums.append(n)
        
    return result


'''
Subset

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def subsets(self, nums: List[int]) -> List[List[int]]:
    
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
            
        subset.append(nums[i])

        dfs(i+1)
        
        subset.pop()
        dfs(i+1)
    
    dfs(0)
    return res