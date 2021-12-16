class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        ans=0
        for i in range(r):
            for j in range(c):
                matrix[i][j]=int(matrix[i][j])
                if(matrix[i][j]==0):
                    continue
                if(i==0 or j==0):
                    ans=max(ans,matrix[i][j])
                    continue
                matrix[i][j]=1+min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
                ans=max(ans,matrix[i][j])
        return ans*ans 




def maximalSquare(matrix: [[str]]) -> int:
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    max_side_len = 0
    memo = {}
    
    def dp(row, col):
        # Base Case: when reaching a not possible cell, return 0
        if row < 0 or row  >= n_rows or col < 0 or col >= n_cols or matrix[row][col] == '0':
            return 0
        
        if (row, col) not in memo:
            # 1 is added because we have already found a suare of len 1(current cell)
            memo[(row, col)] = min(dp(row+1, col), dp(row, col+1), dp(row+1, col+1))+1
        return memo[(row, col)]
        

    for r in range(n_rows):
        for c in range(n_cols):
            if matrix[r][c] == '1':
                curr_side_len = dp(r, c)
                max_side_len = max(max_side_len, curr_side_len)
    # area is side_len to the power of 2
    return max_side_len**2