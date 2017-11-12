class Solution(object):
  def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    if not path:
      return ""
    li = [i for i in path.split('/') if i and i != '.']
    s = []
    for item in li:
      if item != "..":
        s.append(item)
      elif s:
        s.pop()
    return "/" + "/".join(s)
