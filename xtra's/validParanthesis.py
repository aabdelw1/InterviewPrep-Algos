def isValid(s: str) -> bool:
  if len(s) % 2 == 1:
    return False

  opened = ["(", "{", "["]
  closed = [")", "}", "]"]
  stack = []


  for i in s:
    if i in opened:
      stack.append(i)
    elif i in closed:
      pos = closed.index(i)

      if len(stack) > 0 and opened[pos] == stack[-1]:
        stack.pop()
      else: 
        return False

  if len(stack) == 0:
    return True
  
  return False
    
 
print(isValid('()')) #true
print(isValid('(()')) #false
print(isValid('([[]])')) # true