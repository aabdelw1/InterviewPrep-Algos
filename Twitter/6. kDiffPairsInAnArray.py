class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Since we're getting the abs difference between pairs, and we want to return unique pairs,
        # order doesn't matter in array. We also don't want duplicate pairs, so convert nums to a set.
        # Use a hashmap to keep track of each number in the array to see whether each number can make a pair.
        # Edge case: However, if there's 2+ numbers in the list and k == 0, then that should be a pair.
        # We need to use a counter to keep track of this instead of just a set.
        
        numsCounter = Counter(nums)
        pairs = 0
        seen = set()
        
        for val, count in numsCounter.items():
            if k == 0 and count >= 2:
                pairs += 1
            if val + k in seen:
                pairs += 1
            if val - k in seen:
                pairs += 1
                            
            seen.add(val)
        
        return pairs