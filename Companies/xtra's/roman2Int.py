def romanToInt(self, s: str) -> int:
    
    integers = { 
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    lenstr = len(s) - 1
    i = 0
    while i <= lenstr:
        if i != len(s)-1:
            if integers[s[i]] < integers[s[i+1]]:
                num = num + (integers[s[i+1]] - integers[s[i]])
                i = i + 2
            else:
                num = num + integers[s[i]]
                i = i + 1
        else: 
            num = num + integers[s[i]]
            i = i + 1
    return num