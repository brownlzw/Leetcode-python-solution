# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    self.dfs(res, root, 0)
    return res

    if not root:
      return []
    res = []
    level = [root]
    while level:
      res.append([n.val for n in level])

      tmp = []
      for n in level:
        tmp.append(n.left)
        tmp.append(n.right)
      level = [leaf for leaf in tmp if leaf]
    return res

def dfs(self, res, root, level):
    if not root:
      return
    if level == len(res):
      res.append([root.val])
    else:
      res[level].append(root.val)
    self.dfs(res, root.left, level + 1)
    self.dfs(res, root.right, level + 1)