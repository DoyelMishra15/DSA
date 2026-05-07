class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res={}
        s=[]
        prev=-1
        for i in range(len(nums2)-1,-1,-1):
            while s and s[-1]<=nums2[i]:
                s.pop()
            if not s:
                res[nums2[i]]=-1
            else:
                res[nums2[i]]=s[-1]
            s.append(nums2[i])
        ans=[]
        for i in nums1:
            ans.append(res[i])
        return ans
