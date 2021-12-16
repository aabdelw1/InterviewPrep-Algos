def kthFactor(n: int, k: int) -> int:
  count = 0
  for i in range(1, n+1):
      if n %i == 0:
          count += 1
  if count == k:
          return i
  return -1

  #brute force
  factors = []
  for i in range(1,n+1):
      if n % i == 0:
          factors.append(i)
  
  if k > len(factors):
      return -1
  return factors[k-1]

