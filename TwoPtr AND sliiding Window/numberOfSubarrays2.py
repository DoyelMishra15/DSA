class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        curr = 0
        cnt = 0
        for num in nums:
            curr += num % 2
            if curr - k in d:
                cnt += d[curr - k]
            d[curr] = d.get(curr, 0) + 1
        return cnt
