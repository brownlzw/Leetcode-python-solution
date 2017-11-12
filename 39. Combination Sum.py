class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(res, pos, remain, li):
            if not remain:
                res.append(li)
                return
            for i in xrange(pos, len(candidates)):
                if candidates[i] > remain:
                    break
                li.append(candidates[i])
                dfs(res, i, remain - candidates[i], li)
                li.pop()

        candidates.sort()
        res = []
        dfs(res, 0, target, [])
        return res
    # O(k * 2^n'), O(...)