class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1
        while l < r and u < d:
            ans.extend([matrix[u][j] for j in xrange(l, r)])
            ans.extend([matrix[i][r] for i in xrange(u, d)])
            ans.extend([matrix[d][j] for j in xrange(r, l, -1)])
            ans.extend([matrix[i][l] for i in xrange(d, u, -1)])
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            ans.extend([matrix[i][r] for i in xrange(u, d + 1)])
        elif u == d:
            ans.extend([matrix[u][j] for j in xrange(l, r + 1)])
        return ans

        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])