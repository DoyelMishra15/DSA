class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [-1] * n
        s = []
        for i in range(n):
            for j in range(i+1,i+n):
                idx=j%n
                if nums[idx]>nums[i]:
                    res[i]=nums[idx]
                    break
        return res


