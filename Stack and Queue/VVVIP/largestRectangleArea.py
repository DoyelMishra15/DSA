class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = [-1] * n
        s = []
        for i in range(n):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                pse[i] = s[-1]

            s.append(i)
        nse = [n] * n
        s = []
        for i in range(n - 1, -1, -1):

            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                nse[i] = s[-1]
            s.append(i)
        maxi = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            maxi = max(maxi, area)
        return maxi
