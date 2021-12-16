class Solution(object):
    def mostVisitedPattern(self, usernames, timestamps, websites):
        
        data = []
        history = collections.defaultdict(list)
        counter = collections.Counter()
        maxCount = 0
        
        for i in xrange(len(usernames)):
            username = usernames[i]
            timestamp = timestamps[i]
            website = websites[i]
            data.append((timestamp, website, username))
            
        data = sorted(data)
        
        for _, website, username in data:
            history[username].append(website)
        
        for username in history:
            for comb in self.getCombination(history[username]):
                counter[comb] += 1
                maxCount = max(maxCount, counter[comb])
        
        for comb in sorted(counter.keys()):
            if counter[comb]==maxCount: return comb
    
    def getCombination(self, websites):
        def helper(comb, i):
            if len(comb)==3:
                combs.add(tuple(comb[:]))
            elif len(comb)>3 or i>=len(websites):
                return
            else:
                helper(comb+[websites[i]], i+1)
                helper(comb[:], i+1)
                
        combs = set()
        helper([], 0)
        return combs

 def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        combArr = []
        
        for i in range(len(username)):
            combArr.append((timestamp[i], username[i], website[i]))
            
        combArr.sort()

        helperDict = defaultdict(list)
        for i in range(len(helper)):
            t, u, w = combArr[i]
            helperDict[u].append(w)
        
        pattern = defaultdict(int)
        
        for u in helperDict.keys():
            possible_pattern = set(combinations(helperDict[u], 3))
            for p in possible_pattern:
                pattern[p] += 1
        
        points = 0
        popular_pattern = []
        for k,v in pattern.items():
            if points < v:
                points = v
                popular_pattern = [k]
            elif v == points:
                points = v
                popular_pattern.append(k)
        
        popular_pattern.sort()
        return popular_pattern[0]