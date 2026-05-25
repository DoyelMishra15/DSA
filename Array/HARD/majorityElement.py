class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        res=[]
        for x in d:
            if d[x]>n//3:
                res.append(x)
        return res
