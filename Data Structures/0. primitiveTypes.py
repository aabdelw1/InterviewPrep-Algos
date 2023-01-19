#Chapter 4 Problems: 1,7
#Completed: 1,


'''Primitive Types'''

'''
The following program tests bits one -at-a-time starting the
least significant bit. It illustrates shifting and masking it 
also shows how to avoid hard-coding the size of the integer word
'''
def count_bits(x: int) -> int:
  num_bits = 0
  while x:
    num_bits += x & 1
    x >>= 1
  return num_bits

print(count_bits(112342340))


'''Sort Array by Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.'''

def sortArrayByParity(self, nums: List[int]) -> List[int]:
    nums.sort(key = lambda x: x % 2)
    return nums


def sortArrayByParity(self, nums: List[int]) -> List[int]:
    return ([x for x in nums if x % 2 == 0] + 
            [x for x in nums if x % 2 != 0])

def sortArrayByParity(self, nums: List[int]) -> List[int]:

    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] % 2 > nums[r] % 2:
            nums[l], nums[r] = nums[r], nums[l]

        if nums[l] % 2 == 0: l += 1
        if nums[r] % 2 == 1: r -= 1
    return nums


'''
4.1 Computing the Parity of a word

The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise it is 0

How would you compute the parity of a very large number of 64-bit words?
'''
# O(n)
def parity(x: int) -> int:
  result = 0
  while x:
    result ^= x & 1
    x >> 1
  return result

#O(k) where k is the number of bits set to 1 in a particular word
def parity(x: int) -> int:
  result = 0
  while x:
    result ^= x & 1
    x &= x -1
  return result


'''
4.7 Compute pow(x, n)

Write a program that takes a double x and an integer y and returns x^y'''

def myPow(self, x, y):
  result, power = 1.0, y
  if y < 0:
    power, x = -power, 1.0 / x
  while power:
      if power & 1:
          result *= x
      x, power = x * x, power >> 1 
  return result 