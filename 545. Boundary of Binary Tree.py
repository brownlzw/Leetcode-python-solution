# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def boundaryOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
      return []
    res = [root.val]
    if not root.left and not root.right:
      return res
    cur = root.left
    while cur:
      if cur.left or cur.right:
        res.append(cur.val)
      if cur.left:
        cur = cur.left
      else:
        cur = cur.right
    self.dfs(res, root)
    r = []
    cur = root.right
    while cur:
      if cur.left or cur.right:
        r.append(cur.val)
      if cur.right:
        cur = cur.right
      else:
        cur = cur.left
    r.reverse()
    return res + r

  def dfs(self, res, root):
    if not root.left and not root.right:
      res.append(root.val)
    if root.left:
      self.dfs(res, root.left)
    if root.right:
      self.dfs(res, root.right)