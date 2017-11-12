class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def dfs(res, s, num, pos, prev, target):
            if pos == len(num):
                if target == prev:
                    res.append(s)
                return
            cur = 0
            for i in xrange(pos, len(num)):
                cur = 10 * cur + int(num[i])
                if prev is None:
                    dfs(res, num[pos: i + 1], num, i + 1, cur, target)
                else:
                    dfs(res, s + "+" + num[pos: i + 1], num, i + 1, cur, target - prev)
                    dfs(res, s + "-" + num[pos: i + 1], num, i + 1, -cur, target - prev)
                    dfs(res, s + "*" + num[pos: i + 1], num, i + 1, prev * cur, target)
                if num[pos] == '0':
                    break

        res = []
        dfs(res, "", num, 0, None, target)
        return res
