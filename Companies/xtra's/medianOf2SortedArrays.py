def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
  nums1.extend(nums2)
  nums1.sort()
  medium = 0.
  length = len(nums1)
  
  if length % 2 == 0:
      medium = ( nums1[(length//2) - 1] + nums1[length//2] )/2
  else:
      medium = nums1[(len(nums1)//2)]
  
  return medium