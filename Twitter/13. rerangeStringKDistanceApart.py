"""
Time: O(N). N is the number of char in string s. See below explanation.
Space: O(1)

The main idea is to add k different char to the ans every time.
The char with higher count will be used first.
So there will be more different kind of char left and will not be too close to each other.

To do this, we need a counter to track count of each char. [0]
And a heap so we can get the char with highest count fast (LogH). [0]
For each time, add k different char to the ans. [1]
Char with count>0 will be put back to h. [2]

If heap is drained before we add k element to the ans. It is not possible to form ans. Return emptry string. [3]

Time complexity:
Contruct counter takes O(N).
Contruct the heap (heapify) takes O(H), H is the number of element in the heap.
In the while loop, each char in s will be pop once. O(NLogH).
Since the problem said that the string will only have lower case letters. So H will at most be 26.
So O(N+H+NlogH) ~= O(N+26+NLog26) ~= O(N)
"""
class Solution(object):
    def rearrangeString(self, s, k):
        if k==0: return s
        ans = ''
        
		#[0]
        counter = collections.Counter(s)
        h = [(-counter[c], c) for c in counter]
        heapq.heapify(h)
        
        while h:
            l = []
            for i in xrange(k):
                _, c = heapq.heappop(h)
                ans += c
                counter[c] -= 1
                if counter[c]!=0: l.append((-counter[c], c)) #[2]
                
                if len(ans)==len(s): return ans
                if not h and i!=k-1: return '' #[3]
            
            for e in l: heapq.heappush(h, e)
        
        return ans #this line should never be executed
		
"""
Related Heap Problems:
Top K Frequent Elements
Meeting Rooms II, Meeting Rooms
Range Addition
Merge k sorted arrays
Merge k Sorted Lists
Rearrange String k Distance Apart
Minimum Cost to Hire K Workers

For more other topics similar problems, check out my GitHub.
It took me a lots of time to make the solution. Becuase I want to help others like me.
Please give me a star if you like it. Means a lot to me.
https://github.com/wuduhren/leetcode-python
"""




class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        from collections import Counter
        chars = Counter(s)

        # using a max heap to track characters with highest frequency
        # and an array to temporarily store popped heap elements, which will
        # be pushed back to heap later, this question is somehow similar to 
        # problem 621. Task Scheduler
        from heapq import heappush, heappop
        heap = []
        popped = []
        new_str = ''
        for char, count in chars.items():
            heappush(heap, (-count, char))

        while heap:
            for _ in range(k):
                if heap:
                    count, char = heappop(heap)
                    count *= -1
                    # if character appeared in new_str[-k+1:]
                    # then we can not form a new string with
                    # at least k distance, return empty string
                    if char in new_str[-k+1:]:
                        return ''
                    new_str += char
                    count -= 1
                    if count > 0:
                        popped.append((-count, char))
            while popped:
                heappush(heap, popped.pop())

        return new_str