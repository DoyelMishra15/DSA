class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def rec(idx,target,li):
            if target==0:
                res.append(li[:])
                return
            if idx >= len(candidates) or target < 0:
                return
            li.append(candidates[idx])
            rec(idx,target-candidates[idx],li)
            li.pop()
            rec(idx+1,target,li)
        rec(0,target,[])
        return res
