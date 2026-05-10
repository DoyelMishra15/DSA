class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        def rec(idx,nums,li):
            res.append(li[:])
            for i in range(idx,n):
                if i!=idx and nums[i]==nums[i-1]: continue
                li.append(nums[i])
                rec(i+1,nums,li)
                li.pop()
        rec(0,nums,[])
        return res
