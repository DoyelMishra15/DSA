class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m=len(image),len(image[0])
        src_col=image[sr][sc]
        if src_col == color:
            return image
        def fill(i,j):
            if i<0 or i>=n or j<0 or j>=m or image[i][j]!=src_col:
                return
            image[i][j]=color
            fill(i+1,j)
            fill(i-1,j)
            fill(i,j+1)
            fill(i,j-1)
        fill(sr,sc)
        return image
