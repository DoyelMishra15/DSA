class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lm=rm=total=0
        l=0
        r=n-1
        while l<r:
            if height[l]<=height[r]:
                if lm>height[l]:
                    total+=lm-height[l]
                else:
                    lm=height[l]
                l+=1
            else:
                if rm>height[r]:
                    total+=rm-height[r]
                else:
                    rm=height[r]
                r-=1
        return total
