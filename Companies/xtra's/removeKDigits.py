def removeKdigits(self, num: str, k: int) -> str:
        digits = list(num)
        
        for _ in range(k):
            
            # remove first non-monotonic upward digit.
            for i in range(len(digits)):
                if ( i == len(digits)-1 ) or ( int(digits[i]) > int(digits[i+1]) ):
                    digits.pop(i)
                    break
            
            while digits and ( int(digits[0]) == 0 ):
                digits.pop(0)
            
            if len(digits)==0:
                return "0"          
        
        return "".join(digits)
		```



            # Base Case
        if len(nums) == k:
            return "0"
        
        # Init
        m = len(nums)
        
        # Build a monotonic stack, by removing
        # greater element previous to current
        # index
        stack = []
        for i in range(m):
            if stack:
                curr = int(nums[i])
                while k and stack and int(stack[-1]) > curr:
                    stack.pop()
                    k -= 1
            stack.append(nums[i])
        
        # Pop remaining k elements,
        # as they will be greatest in the
        # monotonic stack so created
        while k and stack:
            stack.pop()
            k -= 1
        
        # Join all the element in the stack
        # and first convert it to int, to
        # remove the leading zeros, and
        # then convert to string before
        # returning
        return str(int("".join(stack)))