def minMoves(self, nums: List[int]) -> int:
  #method 1
  m=min(nums)
  s=0
  for i in nums:
      s+=i-m
      
  return s      
  
  #method 2
  minimum = min(nums)
  return sum(num-minimum for num in nums)


  #method 3
  nums.sort()
  N = len(nums)
  target = nums[N//2]
  s = 0
  for n in nums:
    s += (target - n)
  return s

  return sum(abs(target-n) for n in nums)

