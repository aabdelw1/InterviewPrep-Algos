def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:            
    ans = [0] * k
    fmap = collections.defaultdict(list)
    
    for i, x in logs:
        fmap[i].append(x)
    
    
    for i in fmap:
        fmap[i] = list(set(fmap[i]))
        
    print(fmap.keys())
    
    for key, value in fmap.iteritems():
        ans[len(fmap[value]) - 1] += 1
        
    return ans
