def intToRoman(num):
  numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
  symbols = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
  

  num = 3400
  i = 12
  roman =""
  while num > 0:
      div = num // numbers[i]
      num %= numbers[i]
      
      while div > 0:
          roman += symbols[i]
          div = div - 1
          
      i -= 1
  
  return roman