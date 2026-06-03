class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n

        def mem(i):
            if i < 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            dp[i] = max(
                mem(i - 1),
                nums[i] + mem(i - 2)
            )

            return dp[i]

        return mem(n - 1)
