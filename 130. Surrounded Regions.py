class Solution(object):
  def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    n = len(board)
    if n <= 2: return

    m = len(board[0])
    if m <= 2: return

    def dfs(i, j):
      s = [(i, j)]
      while s:
        p, q = s.pop()
        board[p][q] = 'B'
        if p > 0 and board[p - 1][q] == 'O': s += (p - 1, q),
        if p < n - 1 and board[p + 1][q] == 'O': s += (p + 1, q),
        if q > 0 and board[p][q - 1] == 'O': s += (p, q - 1),
        if q < m - 1 and board[p][q + 1] == 'O': s += (p, q + 1),

    for j in xrange(m):
      if board[0][j] == 'O': dfs(0, j)
      if board[n - 1][j] == 'O': dfs(n - 1, j)

    for i in xrange(1, n - 1):
      if board[i][0] == 'O': dfs(i, 0)
      if board[i][m - 1] == 'O': dfs(i, m - 1)

    for i in xrange(n):
      for j in xrange(m):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == 'B':
          board[i][j] = 'O'