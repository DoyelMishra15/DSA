class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def rec(idx,target,li):
            if target==0:
                if li not in res:
                    res.append(li[:])
                return
            if idx==len(candidates) or target<0:
                return
            li.append(candidates[idx])
            rec(idx+1,target-candidates[idx],li)
            li.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            rec(idx+1,target,li)
        rec(0,target,[])
        return res
