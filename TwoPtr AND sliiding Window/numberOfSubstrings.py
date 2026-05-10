class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        d = {}
        l = 0
        cnt = 0

        for r in range(len(s)):

            d[s[r]] = d.get(s[r], 0) + 1

            while len(d) == 3:

                cnt += len(s) - r

                d[s[l]] -= 1

                if d[s[l]] == 0:
                    del d[s[l]]

                l += 1

        return cnt
