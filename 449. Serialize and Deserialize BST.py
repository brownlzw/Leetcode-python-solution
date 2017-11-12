# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    def r(root):
      if not root:
        res.append("#")
        return
      res.append(str(root.val))
      r(root.left)
      r(root.right)

    res = []
    r(root)
    return ",".join(res)


  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    def rr():
      cur = next(i)
      if cur == '#':
        return None
      node = TreeNode(int(cur))
      node.left = rr()
      node.right = rr()
      return node

    i = iter(data.split(','))
    return rr()


    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))