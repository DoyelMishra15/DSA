class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt=k
        n=len(nums)
        ans=0
        for i in range(n):
            cnt=k
            for j in range(i,n):
                if nums[j]==0:
                    cnt-=1
                if cnt<0:
                    break
                ans=max(ans,j-i+1)
        return ans

  class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt=k
        n=len(nums)
        ans=0
        i=0
        cnt=0
        for j in range(n):
            if nums[j]==0:
                cnt+=1
            while cnt>k:
                if nums[i]==0:
                    cnt-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans
