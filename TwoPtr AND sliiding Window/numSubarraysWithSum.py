class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0: 1}
        curr = 0
        cnt = 0
        for num in nums:
            curr += num
            if curr - goal in d:
                cnt += d[curr - goal]
            d[curr] = d.get(curr, 0) + 1
        return cnt
