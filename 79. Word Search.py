class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False
        m, n = len(board), len(board[0])

        def dfs(x, y, p):
            val = board[x][y]
            if p == len(word):
                return True

            board[x][y] = '#'
            for dx, dy in ((-1, 0), (0, 1), (0, -1), (1, 0)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == word[p] and dfs(nx, ny, p + 1):
                    return True
            board[x][y] = val
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True
        return False
    # O(N^2 * 4^k), O(N^2 * k)
