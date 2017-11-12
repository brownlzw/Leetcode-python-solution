# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def str2tree(self, s):
    """
    :type s: str
    :rtype: TreeNode
    """
    if not s:
      return
    if not s: return None
    s = s.split('(')
    root = TreeNode(int(s[0]))
    stack = [root]
    for i in xrange(1, len(s)):
      v = s[i].rstrip(')')
      new = TreeNode(int(v))
      if stack[-1].left:
        stack[-1].right = new
      else:
        stack[-1].left = new
      nr = len(s[i]) - len(v)
      if nr == 0:
        stack.append(new)
      for _ in xrange(nr - 1):
        stack.pop()
    return root
