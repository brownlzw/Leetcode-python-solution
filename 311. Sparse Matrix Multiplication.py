class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        d1, d2, d3 = len(A), len(B), len(B[0])
        C = [[0] * d3 for _ in xrange(d1)]
        for i in xrange(d1):
            if not any(A[i]):
                continue
            for j in xrange(d2):
                if A[i][j] == 0:
                    continue
                for k in xrange(d3):
                    C[i][k] += A[i][j] * B[j][k]
        return C
