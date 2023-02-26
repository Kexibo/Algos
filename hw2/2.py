#O(n)
def getMaximumGenerated(n):
        if n == 0:
            return 0
    
        dp = [0] * (n+1)
        dp[1] = 1
        maximum = 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2+1]
            maximum = max(maximum, dp[i])
        
        return maximum

print(getMaximumGenerated(7))
