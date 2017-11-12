class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(res, pos, remain, li):
            if not remain:
                res.append(li[:])
                return
            for i in xrange(pos, len(candidates)):
                if candidates[i] > remain:
                    break
                if i != pos and candidates[i] == candidates[i - 1]:
                    continue
                li.append(candidates[i])
                dfs(res, i + 1, remain - candidates[i], li)
                li.pop()

        candidates.sort()
        res = []
        dfs(res, 0, target, [])
        return res