from collections import defaultdict,deque
class Solution(object):
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    indegree = [0] * numCourses
    child = defaultdict(list)
    for item in prerequisites:
      a, b = item[0], item[1]
      if a == b:
        return False
      indegree[a] += 1
      child[b].append(a)
    zero = deque([i for i,c in enumerate(indegree) if c == 0])
    count = 0
    while zero:
      cur = zero.popleft()
      count += 1
      for c in child[cur]:
        indegree[c] -= 1
        if not indegree[c]:
          zero.append(c)
      child.pop(cur)
    return count == numCourses