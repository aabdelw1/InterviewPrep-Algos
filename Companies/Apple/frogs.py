import numpy as np



def solution(A):
    n = len(A)
    result = 0
    for i in range(n):
        j = i 
        # move left while A are less than or equal to current block
        while j > 0 and A[j-1] >= A[j]:
            j -= 1
        low = j
        j = i
        # move right while A are less than or equal to current block
        while j < n-1 and A[j+1] >= A[j]:
            j += 1
        high = j
        result = max(result, high - low)
    return result



print(solution([6,6,7,4,3,1,2,3,7,6]))
# print(solution)

# randnums= np.random.randint(1,8,10)
# print(randnums)