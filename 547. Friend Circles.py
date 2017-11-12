class Solution(object):
  def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    def dfs(i):
      for j in xrange(n):
        if M[i][j] and not visited[j]:
          visited[j] = True
          dfs(j)

    n = len(M)
    visited = [False] * n
    count = 0
    for i in xrange(n):
      if not visited[i]:
        visited[i] = True
        count += 1
        dfs(i)
    return count



  #   m = [i for i in xrange(n)]
  #
  #   for i in  xrange(n):
  #     for j in xrange(i + 1, n):
  #       if M[i][j]:
  #         self.union(m, i, j)
  #   return sum([i == m[i] for i in xrange(n)])
  #
  # def union(self, m, i, j):
  #   while i != m[i]:
  #     i = m[i]
  #   while j != m[j]:
  #     j = m[j]
  #   if i != j:
  #     m[i] = j