class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        res = [[0] * n for _ in xrange(n)]
        cnt = 1
        u, d, l, r = 0, n - 1, 0, n - 1
        while l < r and u < d:
            for j in xrange(l, r):
                res[u][j] = cnt
                cnt += 1
            for i in xrange(u, d):
                res[i][r] = cnt
                cnt += 1
            for j in xrange(r, l, -1):
                res[d][j] = cnt
                cnt += 1
            for i in xrange(d, u, - 1):
                res[i][l] = cnt
                cnt += 1
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            for i in xrange(u, d + 1):
                res[i][r] = cnt
                cnt += 1
        elif u == d:
            for j in xrange(l, r + 1):
                res[u][j] = cnt
                cnt += 1
        return res

        A = [[0] * n for i in range(n)]
        r, c, dr, dc = 0, 0, 0, 1
        for i in range(n * n):
            A[r][c] = i + 1
            if A[(r + dr) % n][(c + dc) % n]:
                dr, dc = dc, -dr
            r += dr
            c += dc
        return A
