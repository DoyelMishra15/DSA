class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==len(cardPoints):
            return sum(cardPoints[:])
        else:
            lsum = sum(cardPoints[0:k])
            rsum, s=0,lsum
            for i in range(k-1,-1,-1):
                lsum = lsum - cardPoints[i]
                rsum= rsum + cardPoints[len(cardPoints) - k + i]
                s = max(s,lsum+rsum)
            return s
