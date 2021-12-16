def longestPalindrome(self, s: str) -> str:
    curr = ""
    longest = ""
    for i in range(len(s)):
        
        #odd cases
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr = s[left:right+1]
            if len(curr) > len(longest):
                longest = curr
                
            left = left - 1
            right = right + 1
                
        left, right = i, i+1 
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr = s[left:right+1]
            if len(curr) > len(longest):
                longest = curr
            left = left - 1
            right = right +1
    return longest
                        