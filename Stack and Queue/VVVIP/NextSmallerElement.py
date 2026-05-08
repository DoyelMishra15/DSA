class Solution:
    def nextSmallerElement(self, nums):
        n = len(nums)
        res = [-1] * n
        s = []

        for i in range(n - 1, -1, -1):

            while s and s[-1] >= nums[i]:
                s.pop()

            if s:
                res[i] = s[-1]

            s.append(nums[i])

        return res
