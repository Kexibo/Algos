#O(mn) 
def countSquares(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    count = 0
    
    for i in range(m):
        dp[i][0] = matrix[i][0]
        count += dp[i][0]
    for j in range(1, n):
        dp[0][j] = matrix[0][j]
        count += dp[0][j]
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                count += dp[i][j]
    
    return count
print(countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
