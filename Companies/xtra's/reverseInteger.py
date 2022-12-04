def reverse(self, x: int) -> int:
  negative = False
  if x < 0:
    negative = True
    x = x * -1
  
  y = str(x)
  new = ""
  
  for i in range(len(y), 0, -1):
    new += y[i-1]

  
  if int(new) <= -pow(2,31) or int(new) >= pow(2,31)-1:
    return 0 
  
  if negative:
    return int(new) * -1
  
  return int(new)