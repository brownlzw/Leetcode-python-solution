class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, last_i, last_j, pair):
            cnt = 0
            for i in xrange(last_i, len(s)):
                cnt += (s[i] == pair[0]) - (s[i] == pair[1])
                if cnt < 0:
                    for j in xrange(last_j, i + 1):
                        if s[j] == pair[1] and (j == last_j or s[j - 1] != pair[1]):
                            # still i, j because we removed one! i, j is actual the next unvisited index
                            dfs(s[:j] + s[j + 1:],i, j, pair)
                    return
            s = s[::-1]
            if pair[0] == '(':
                dfs(s, 0, 0, [')', '('])
            else:
                res.append(s)

        res = []
        dfs(s, 0, 0, ['(', ')'])
        return res
    # O(2 ^ n), O(n^2)