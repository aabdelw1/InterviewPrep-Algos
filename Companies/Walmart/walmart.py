
def commonChars(self, words: List[str]) -> List[str]:
    data = collections.Counter(words[0])
    for word in words:
        data2 = collections.Counter(word)
        for k in data.keys():
            data[k] = min(data[k], data2[k])
    return data.elements()


def longestCommonPrefix(self, strs: List[str]) -> str:
    
    
    shortest = min(strs, key=len)
    pres = ""
    for i, ch in enumerate(shortest):
        for others in strs:
            if others[i] != ch:
                return shortest[:i]
            
    return shortest