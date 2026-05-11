class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at(nums,k)-self.at(nums,k-1)
    def at(self, nums: List[int], k: int) -> int:
        d={}
        l=0
        cnt=0
        prevcnt=0
        for right in range(len(nums)):
            d[nums[right]]=d.get(nums[right],0)+1
            while len(d)>k:
                if d[nums[l]]-1==0:
                    del d[nums[l]]
                else:
                    d[nums[l]]-=1
                l+=1
            prevcnt=cnt
            cnt+=right-l+1
        return cnt
