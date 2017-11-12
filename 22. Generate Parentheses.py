class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(n1, n2, cur):
            if not n1 and not n2:
                res.append(cur)
            if n1:
                dfs(n1 - 1, n2, cur + '(')
            if n2 > n1:
                dfs(n1, n2 - 1, cur + ')')

        res = []
        dfs(n, n, '')
        return res