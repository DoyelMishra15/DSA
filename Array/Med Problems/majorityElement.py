class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        n=n//2
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
            if d[x]>n:
                return x
