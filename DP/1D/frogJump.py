height=list(map(int,input().split(",")))
n=len(height)
dp=[10**9+7]*(n)
dp[0] = 0
dp[1] = abs(height[1] - height[0])
for i in range(2,n):
    dp[i] = min(dp[i-1] + abs(height[i] - height[i-1]), dp[i-2] + abs(height[i] - height[i-2]))
print(dp[n-1])
