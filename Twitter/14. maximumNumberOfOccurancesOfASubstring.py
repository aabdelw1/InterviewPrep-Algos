class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if not s:
            return 0
        ht,ans = collections.defaultdict(int),0
        
        def generateSlices(s, size, ht):
            for i in range(0,len(s)-size+1):
                ht[s[i:i+size]]+=1
        
        for size in range(minSize, maxSize+1):
            generateSlices(s,size,ht)
            
        for key,val in ht.items():
            if len(set(key))<=maxLetters:
                ans = max(ans,val)
        
        return (ans)
        