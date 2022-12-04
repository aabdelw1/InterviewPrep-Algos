def lengthOfLongestSubstring(self, s: str) -> int:
  sub = {}
  current_sub_length = 0
  current = 0
  longest = 0
  
  for i, letter in enumerate(s):
      if letter in sub and sub[letter] >= current_sub_length:
          current_sub_length = sub[letter] + 1
          current = i - sub[letter]
      else:
          current += 1
          longest = max(longest, current)

      sub[letter] = i
              
  return longest