class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in xrange(0, 9)]
        col = [set() for i in xrange(0, 9)]
        grid = [set() for i in xrange(0, 9)]

        for i in xrange(0, 9):
            for j in xrange(0, 9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                if board[i][j] in col[j]:
                    return False
                g = i / 3 * 3 + j / 3
                if board[i][j] in grid[g]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                grid[g].add(board[i][j])
        return True