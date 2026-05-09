class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        pse = [-1] * n
        nse = [n] * n
        s = []
        # PSE
        for i in range(n):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                pse[i] = s[-1]
            s.append(i)
        s = []
        # NSE
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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        maxi = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            maxi = max(maxi, self.largestRectangleArea(heights))
        return maxi
