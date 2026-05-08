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


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [-1] * n
        s = []
        for i in range(2*n-1, -1, -1):
            while s and s[-1] <= nums[i%n]:
                s.pop()
            if i<n:
                if s:
                    res[i] = s[-1]
                else:
                    res[i]=-1
            s.append(nums[i%n])
        return res
