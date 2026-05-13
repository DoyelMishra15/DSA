#Bruteforce

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

#optimal
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        l=r=0
        jump=0
        while r<n-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(i+nums[i],farthest)
            l=r+1
            r=farthest
            jump+=1
        return jump
