# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def findFrequentTreeSum(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def dfs(root):
      if not root:
        return 0
      left = dfs(root.left)
      right = dfs(root.right)
      cur = left + right + root.val
      if cur not in m:
        m[cur] = 1
      else:
        m[cur] += 1
      if m[cur] > self.maxfreq:
        self.maxfreq, self.maxli = m[cur], [cur]
      elif m[cur] == self.maxfreq:
        self.maxli.append(cur)
      return cur

    m = {}
    self.maxfreq, self.maxli = 0, []
    dfs(root)
    return self.maxli
