class Solution:
    def maxDepth(self, s: str) -> int:
        max_cnt=0
        cnt=0
        for i in s:
            if i=='(':
                cnt+=1
                max_cnt=max(cnt,max_cnt)
            elif i==')':
                cnt-=1
        return max_cnt
