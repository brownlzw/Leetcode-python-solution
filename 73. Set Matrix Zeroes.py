class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        firstr, firstc = not all(matrix[0]), matrix[0][0] == 0
        for i in xrange(1, m):
            firstc = firstc or not matrix[i][0]
            for j in xrange(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0
        for i in xrange(1, m):
            if not matrix[i][0]:
                matrix[i] = [0] * n
        for j in xrange(1, n):
            if not matrix[0][j]:
                for row in matrix:
                    row[j] = 0
        if firstr:
            matrix[0] = [0] * n
        if firstc:
            for row in matrix:
                row[0] = 0
    # O(n^2), O(1)

        row_zero = [1] * len(matrix)
        col_zero = [1] * len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_zero[i] = 0
                    col_zero[j] = 0
        for i in xrange(len(row_zero)):
            if row_zero[i] == 0:
                for j in xrange(len(matrix[0])):
                    matrix[i][j] = 0
        for i in xrange(len(col_zero)):
            if col_zero[i] == 0:
                for j in xrange(len(matrix)):
                    matrix[j][i] = 0
