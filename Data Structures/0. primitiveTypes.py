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

