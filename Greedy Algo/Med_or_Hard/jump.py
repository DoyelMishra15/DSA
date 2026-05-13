class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        def rec(idx,jump):
            if idx>=n-1:
                return jump
            mini=10**9
            for i in range(1,nums[idx]+1):
                mini=min(mini,rec(idx+i,jump+1))
            return mini
        return rec(0,0)
