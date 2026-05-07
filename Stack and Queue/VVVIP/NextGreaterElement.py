class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in range(len(nums2)):
            d[nums2[i]]=i
        res=[]
        for i in nums1:
            for j in range(d[i]+1,len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res
