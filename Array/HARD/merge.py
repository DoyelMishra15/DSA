class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 1
        intervals.sort()
        ans=intervals[0]
        temp=intervals[0]
        while i<n:
            if intervals[i][0]<=ans[1]:
                if intervals[i][1] > ans[1]:
                        ans[1] = intervals[i][1]
            else:
                res.append(ans)
                ans=intervals[i]
            i+=1
        res.append(ans)
        return res
