class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums2)
        s=[]
        prev=-1
        for i in range(len(nums2)-1,-1,-1):
            while s and s[-1]<=nums[i]:
                s.pop()
            if not s:
                res[i]=-1
            else:
                res[i]=s.pop()
            s.append(nums2[i])
        return res
