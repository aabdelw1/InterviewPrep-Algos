'''
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
of rows like this: (you may want to display this pattern in a fixed font for better legibility)'''


def convert(self, s: str, numRows: int) -> str:
    
    if numRows == 1: return s
    
    res = ""
    for r in range(numRows):
        increment = (numRows-1) * 2
        for i in range(r, len(s), increment):
            res += s[i]
            if r > 0 and r < numRows - 1 and i + increment - 2 *r < len(s):
                res += s[i + increment - 2 *r]
                
    return res