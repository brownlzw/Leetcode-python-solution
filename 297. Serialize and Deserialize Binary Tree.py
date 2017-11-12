# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # def serialize(self, root):
    #   """Encodes a tree to a single string.
    #
    #   :type root: TreeNode
    #   :rtype: str
    #   """
    #   if not root:
    #     return ''
    #   path = []
    #   self.serilize_helper(root, path)
    #   return ",".join(path)
    #
    # def serilize_helper(self, root, path):
    #   if not root:
    #     path.append("#")
    #     return
    #   path.append(str(root.val))
    #   self.serilize_helper(root.left, path)
    #   self.serilize_helper(root.right, path)
    #
    #
    # def deserialize(self, data):
    #   """Decodes your encoded data to tree.
    #
    #   :type data: str
    #   :rtype: TreeNode
    #   """
    #   if not data:
    #     return None
    #   path = data.split(",")
    #   root =  TreeNode(int(path[0]))
    #   stack = []
    #   cur = root
    #   i = 1
    #   while stack or cur:
    #     while cur:
    #       stack.append(cur)
    #       cur.left = None if path[i] == "#" else TreeNode(int(path[i]))
    #       cur = cur.left
    #       i += 1
    #     cur = stack.pop()
    #     cur.right = None if path[i] == "#" else TreeNode(int(path[i]))
    #     cur = cur.right
    #     i += 1
    #   return root

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vlist = []

        def r(root):
            if root is not None:
                vlist.append(str(root.val))
                r(root.left)
                r(root.right)
            else:
                vlist.append('?')

        r(root)
        return ' '.join(vlist)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rr():
            val = data[index[0]]
            index[0] += 1
            if val != '?':
                t = TreeNode(int(val))
                t.left = rr()
                t.right = rr()
                return t
            else:
                return None

        input = iter(data.split())
        index = [0]
        return rr()

        # BFS:
        # def serialize(self, root):
        #   """Encodes a tree to a single string.
        #
        #   :type root: TreeNode
        #   :rtype: str
        #   """
        #   if not root: return ''
        #   queue = [root]
        #   res = []
        #   while queue:
        #     tmp = []
        #     for x in queue:
        #       if x:
        #         res.append(str(x.val))
        #         tmp.append(x.left)
        #         tmp.append(x.right)
        #       else:
        #         res.append('#')
        #     queue = tmp
        #   return ' '.join(res)
        #
        # def deserialize(self, data):
        #   """Decodes your encoded data to tree.
        #
        #   :type data: str
        #   :rtype: TreeNode
        #   """
        #   if not data: return None
        #   data = data.split()
        #   index = 1
        #   root = TreeNode(data[0])
        #   queue = [root]
        #   while queue:
        #     tmp = []
        #     for x in queue:
        #       if data[index] != '#':
        #         x.left = TreeNode(data[index])
        #         tmp.append(x.left)
        #       index += 1
        #       if data[index] != '#':
        #         x.right = TreeNode(data[index])
        #         tmp.append(x.right)
        #       index += 1
        #     queue = tmp
        #   return root



        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
