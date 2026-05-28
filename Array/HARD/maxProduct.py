class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp = curMax

            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * temp, n * curMin)

            ans = max(ans, curMax)

        return ans
