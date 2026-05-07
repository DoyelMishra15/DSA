class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        curr = 0
        count = 0
        for num in nums:
            curr += num
            if curr - k in d:
                count += d[curr - k]
            d[curr] = d.get(curr, 0) + 1
        return count
