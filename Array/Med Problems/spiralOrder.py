class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        top,left=0,0
        bottom=n-1
        right=m-1
        res=[]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1

            for j in range(top,bottom+1):
                res.append(matrix[j][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            
            if left<=right:
                for j in range(bottom,top-1,-1):
                    res.append(matrix[j][left])
                left+=1

        return res
