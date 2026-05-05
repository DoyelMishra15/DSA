class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        t = copy.deepcopy(matrix)
        for i in range(len(t)):
            for j in range(len(t[0])):
                if t[i][j] == 0:
                    for k in range(len(t[0])):
                        matrix[i][k] = 0
                    for r in range(len(t)):
                        matrix[r][j] = 0
