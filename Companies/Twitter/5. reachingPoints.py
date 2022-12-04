class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx or sy < ty: 
            if tx > ty: 
                k = (tx - sx)//ty 
                if k == 0: break 
                tx -= k * ty 
            else: 
                k = (ty - sy)//tx 
                if k == 0: break 
                ty -= k * tx 
        return sx == tx and sy == ty


##method 2 

'''
Work Backwards
The first approach came to my mind is to use resucrsion + memoization, which is standard approach to searching problems, and exceeds time limits.
 We have to improve this approach, first of which is to modulus the tx and ty and it works in some cases. We still go to 2 branchs for each move, which keeps the time complexity remained.
Instead of starting with source, we can try to work backwords from target because the larger number must be got by adding the smaller number up to their difference. 
In anther word, there are 2 children for each point, (x, x + y) and (x + y, y), while there is only one parent (x - y, y) for (x, y) when (x > y). Based on this observation, we can go along with the path of target to his parents, and return whether true or false if source is in the path or not.

Besides, we can speed up the process by modulus instead as we will keep subtracting y from x until x < y.
 When either is smaller than or equals to sx or sy, we have to stop this process, and return true if

1. tx == sx and ty == sy
2. tx == sx and ty > sy and (ty - sy) % tx == 0 // tx is not changed, and add times of tx to be equals to ty
3. ty == sy and tx > sx and (tx - sx) % ty == 0 // similar with 2


Time Complexity= O(lg(max(tx, ty)))
Space Complexity= O(1)

'''

def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    while tx > sx and ty > sy:
        if tx > ty:
            tx %= ty 
        else:
            ty %= tx
    if (tx == sx and ty == sy):
        return True



    return (tx == sx and ty == sy) or (tx == sx and ty > sy and not (ty - sy) % tx) or (ty == sy and tx > sx and not (tx - sx) % ty)