from collections import deque
class Solution(object):
  def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    if not rooms or not rooms[0]:
      return

    m = len(rooms)
    n = len(rooms[0])

    q = deque()

    for i in range(m):
      for j in range(n):
        if rooms[i][j] == 0:
          q.append((i, j, 0))

    empty = 2147483647

    while q:
      i, j, d = q.popleft()

      new_distance = d + 1

      # Search up
      if i > 0 and rooms[i - 1][j] == empty:
        rooms[i - 1][j] = new_distance
        q.append((i - 1, j, new_distance))

      # Search down
      if i < m - 1 and rooms[i + 1][j] == empty:
        rooms[i + 1][j] = new_distance
        q.append((i + 1, j, new_distance))

      # Search left
      if j > 0 and rooms[i][j - 1] == empty:
        rooms[i][j - 1] = new_distance
        q.append((i, j - 1, new_distance))

      # Search right
      if j < n - 1 and rooms[i][j + 1] == empty:
        rooms[i][j + 1] = new_distance
        q.append((i, j + 1, new_distance))

    if not rooms or not rooms[0]:
      return
    for i in xrange(len(rooms)):
      for j in xrange(len(rooms[0])):
        if not rooms[i][j]:
          self.bfs(rooms, i, j, 0)

  def bfs(self, rooms, i, j, d):
    if d and rooms[i][j] <= d:
      return
    rooms[i][j] = d
    if i > 0 and rooms[i - 1][j] != -1 and rooms[i - 1][j] != 0:
      self.bfs(rooms, i - 1, j ,d + 1)
    if j > 0 and rooms[i][j - 1] != -1 and rooms[i][j - 1] != 0:
      self.bfs(rooms, i - 1, j ,d + 1)
    if i + 1 < len(rooms) and rooms[i + 1][j] != -1 and rooms[i + 1][j] != 0:
      self.bfs(rooms, i - 1, j ,d + 1)
    if j + 1 < len(rooms[0]) and rooms[i][j + 1] != -1 and rooms[i][j + 1] != 0:
      self.bfs(rooms, i - 1, j ,d + 1)