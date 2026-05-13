class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maz=0
        for i in range(len(nums)):
            if i>maz:
                return False
            maz=max(i+nums[i],maz)
        return True
