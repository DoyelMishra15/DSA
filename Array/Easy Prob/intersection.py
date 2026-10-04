class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        i = 0
        j = 0
        result = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                i += 1

            elif nums1[i] > nums2[j]:
                j += 1

            else:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])

                i += 1
                j += 1

        return result
