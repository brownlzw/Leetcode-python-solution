class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col - 1]
        self.d = matrix

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        n = len(self.d[0])
        original = self.d[row][col]
        if col:
            original -= self.d[row][col - 1]
        diff = val - original
        for i in xrange(col,n):
            self.d[row][i] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in xrange(row1, row2 + 1):
            res += self.d[i][col2]
            if col1:
                res -= self.d[i][col1 - 1]
        return res
    # O(n), O(m)