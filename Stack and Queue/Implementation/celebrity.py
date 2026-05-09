class Solution:
    def celebrity(self, M, n):

        top = 0
        down = n - 1

        while top < down:

            if M[top][down] == 1:
                top += 1
            else:
                down -= 1

        cand = top

        for i in range(n):

            if i != cand:

                if M[cand][i] == 1 or M[i][cand] == 0:
                    return -1

        return cand
