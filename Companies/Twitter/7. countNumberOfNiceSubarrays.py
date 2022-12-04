"""

Example:

2 2 2 1 2 2 2 1 2

1 2 2 2 1 - nice sub-array

begin_count - count of subarrays, that ending on nice subarray:
   2 2 2 1 2 2 2 1
     2 2 1 2 2 2 1
       2 1 2 2 2 1
         1 2 2 2 1

So we have 4 subarrays

When we found all such subarrays, "begin" is equivalent to the index after the start (begin == 4)

While we can`t find new nice sub-array, we will be expand count of sub-arrays so for each even number, we will add begin_count.

   2 2 2 1 2 2 2 1 2

For last element:
   2 2 2 1 2 2 2 1 2
     2 2 1 2 2 2 1 2
       2 1 2 2 2 1 2
         1 2 2 2 1 2

So we have 4 subarrays again.

If we find new nice sub-array, we will repeat the actions again

"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # begin_count - count subarrays, that ending on nice subarray
        begin = begin_count = res = 0
        
        for end in range(len(nums)):
            # if last bit equal 1 - odd
            if nums[end] & 1:
                k -= 1
                begin_count = 0
                
            while k == 0:
                begin_count += 1
                
                if nums[begin] & 1:
                    k += 1
                
                begin += 1
            
            res += begin_count

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
	odd = 0
	dic = defaultdict(int)
	dic[0] = 1
	l = len(nums)
	count = 0

	for i in range(0, l):
		odd+=(nums[i]%2)
		count+=dic[odd-k]
		dic[odd]+=1
	return count

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
  a=[]
  for i in range(0,len(nums)):
      if nums[i]%2==1:
          a.append(i)
  i=0
  count=0
  n=len(a)
  while(i<=n-k):
      j=i+k-1
      if i==0:
          A=-1
      else:
          A=a[i-1]
      
      if j+1==n:
          B=len(nums)
      else:
          B=a[j+1]
          
      ns=(a[i]-A)*(B-a[j])
      
      count=count + ns
      
      i=i+1
  return count
