class Solution(object):
  def findRestaurant(self, list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    m = {}
    for i, s in enumerate(list1):
      m[s] = i
    res, minsum = [], 2 ** 31 - 1
    for i, s in enumerate(list2):
      if s in m:
        if m[s] + i < minsum:
          res, minsum = [s], m[s] + i
        elif m[s] + i == minsum:
          res.append(s)
    return res
