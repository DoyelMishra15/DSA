heights=[10, 5, 20, 0, 15]#list((map(int,input().split(',')))
k=2#int(input())
heights = [10, 5, 20, 0, 15]
k = 2

n = len(heights)
dp = [-1] * n

def mem(i):
    if i == 0:
        return 0

    if dp[i] != -1:
        return dp[i]

    ans = float('inf')

    for j in range(1, k + 1):
        if i - j >= 0:
            cost = mem(i - j) + abs(heights[i] - heights[i - j])
            ans = min(ans, cost)

    dp[i] = ans
    return ans

print(mem(n - 1))
