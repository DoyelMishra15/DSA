class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        n=len(arr)
        s=[]
        for i in range(n):
            if arr[i]>0:
                s.append(arr[i])
            else:
                while s and s[-1]>0 and s[-1]<abs(arr[i]):
                    s.pop()
                if s and s[-1]==abs(arr[i]):
                    s.pop()
                else:
                    if not s or s[-1]<0:
                        s.append(arr[i])
        return s
