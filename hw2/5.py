#o(n)
def getDescentPeriods(prices):
        ans = 1
        dp = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                dp += 1
            else:
                dp = 1
            ans += dp

        return ans
print(getDescentPeriods([3,2,1,4]))
