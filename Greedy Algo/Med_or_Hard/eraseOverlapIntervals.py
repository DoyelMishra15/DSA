class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n=len(intervals)
        # res=[]
        # res.append(intervals[0])
        i=1
        cnt=0
        last=intervals[0]
        while i<n:
            if last[1]<=intervals[i][0]:
                #res.append(intervals[i])
                last=intervals[i]
            else:
                cnt+=1
            i+=1
        return cnt
