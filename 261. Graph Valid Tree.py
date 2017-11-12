class Solution(object):
  def validTree(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    if len(edges) != n - 1:
      return False
    parent = range(n)

    def find(x):
      return x if parent[x] == x else find(parent[x])

    for edge in edges:
      x, y = map(find, edge)
      if x == y:
        return False
      parent[y] = x
    return True

    if len(edges) != n - 1:
      return False
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
      neighbors[v] += w,
      neighbors[w] += v,
    stack = [0]
    while stack:
      stack += neighbors.pop(stack.pop(), [])
    # queue = collections.deque([0])
    # while queue:
    #   queue.extend(neighbors.pop(queue.popleft(), []))

    # def visit(v):
    #   map(visit, neighbors.pop(v, []))
    #
    # visit(0)
    return not neighbors
