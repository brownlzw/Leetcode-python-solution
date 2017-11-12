import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    q = collections.deque()
    q.append(root)
    res = []
    while q:
      levelNum = len(q)
      sumNum = 0
      for i in range(levelNum):
        node = q.popleft()
        sumNum += node.val
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      res.append(sumNum / (levelNum * 1.0))
    return res
