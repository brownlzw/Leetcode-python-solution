from collections import deque
class Solution(object):
  def updateBoard(self, board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    if not board or not board[0]:
      return
    m, n = len(board), len(board[0])
    q = deque([(click[0], click[1])])
    visited = {(click[0], click[1])}
    while q:
      i, j = q.popleft()
      if board[i][j] == 'M':
        board[i][j] = 'X'
        return board
      elif board[i][j] == 'E':
        count = 0
        for r in xrange(-1, 2):
          for c in xrange(-1, 2):
            ii, jj = i + r, j + c
            if 0 <= ii < m and 0 <= jj < n and board[ii][jj] in 'XM':
                count += 1
        if count:
          board[i][j] = str(count)
        else:
          board[i][j] = 'B'
          for r in xrange(-1, 2):
            for c in xrange(-1, 2):
              ii, jj = i + r, j + c
              if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'E' and (ii, jj) not in visited:
                q.append((ii, jj))
                visited.add((ii, jj))
    return board
