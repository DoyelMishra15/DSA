#brute

class Solution:
    def insert(self, intervals: List[List[int]], newIntervals: List[int]) -> List[List[int]]:
        n=len(intervals)
        res=[]
        i=0
        while i<n and intervals[i][1]<newIntervals[0]:
            res.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=newIntervals[1]:
            newIntervals[0]=min(newIntervals[0],intervals[i][0])
            newIntervals[1]=max(newIntervals[1],intervals[i][1])
            i+=1
        res.append(newIntervals)
        while i<n:
            res.append(intervals[i])
            i+=1
        return res
