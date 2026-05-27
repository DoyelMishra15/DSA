class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,x=m-1,m+n-1,n-1
        while i>=0 and x>=0:
            if nums1[i]>nums2[x]:
                nums1[j]=nums1[i]
                i-=1
                j-=1
            else:
                nums1[j]=nums2[x]
                x-=1
                j-=1
        while x >= 0:
            nums1[j] = nums2[x]
            x -= 1
            j -= 1
