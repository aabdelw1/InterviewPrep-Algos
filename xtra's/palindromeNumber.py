def isPalindrome(x: int) -> bool:
  if(x < 0):
      return False
  
  y = str(x)
  st = ""
  for i in range(len(y), 0, -1):
      st += y[i-1]
      
  return int(st) == x 

print(isPalindrome(121))