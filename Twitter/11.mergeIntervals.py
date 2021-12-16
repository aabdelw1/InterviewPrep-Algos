def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the arry
        intervals.sort()
        
        output = []
        
        for i in intervals:
			# output list is empty so nothing to compare to
            if not output:
                output.append(i)
			# i is actually contained within the latest interval in output
            elif output[-1][0] <= i[0] and output[-1][1] >= i[1]:
                pass
			# interval in output and i overlap
            elif output[-1][1] >= i[0]:
                output[-1][1] = i[1]
			# no overlap, start of next interval in output
            else:
                output.append(i)
        
        return output


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # merge overlap
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged