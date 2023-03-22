def maxSetSize(riceBags):
    # Write your code here
    maxCount = []
    count = []
    maps = {}
    setOfRiceBags = set(riceBags)
    for i in range(len(riceBags)):
        if (riceBags[i] ** 1/2).is_integer() and int(riceBags[i] ** 1/2) in setOfRiceBags:
            continue
        maps[riceBags[i]] = [] #initialize hashmap to ricebags that have a square root in the array
        

    for item in maps:
        temp = item
        while temp in setOfRiceBags:
            maps[item].append(temp)
            temp = temp * temp
    
    maxCount = max(len(item) for item in maps.values())
    
    # print(maxCount)

    return maxCount if maxCount >= 2 else -1  

# print(maxSetSize(riceBags))


def invariance(nums):
  all = []
  def printSubArrays(arr, start, end):
     
    # Stop if we have reached the end of the array   
    if end == len(arr):
        return
     
    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)
         
    # Print the subarray and increment the starting
    # point
    else:
        # print(arr[start:end + 1])
        if len(arr[start:end + 1]) > 1:
          all.append(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)
  arr = [4,1,3,2]
  printSubArrays(arr, 0,0)

  def missingNumber(nums):
    l=len(nums)
    m=min(nums)
    for i in range(m,l+1,1):
        if(i not in nums):
            return i
    return 0

  count = 0 
  for i in all:
    
    if missingNumber(i) != 0:
      count += 1 


  print(count)

invariance([4,1,3,2])
