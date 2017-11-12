class Solution(object):
  def validSquare(self, p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    p = [p1, p2, p3, p4]
    d = [0] * 3
    d[0] = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    d[1] = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
    d[2] = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
    maxd = max(d)
    if d.count(maxd) != 1 or d.count(maxd/2) != 2:
      return False
    maxi = d.index(maxd) + 1
    d1 = []
    for pt in p:
      if pt != p[maxi]:
        d1.append((p[maxi][0] - pt[0]) ** 2 + (p[maxi][1] - pt[1]) ** 2)
    maxd2 = max(d1)
    if d1.count(maxd2) != 1 or d1.count(maxd2/2) != 2:
      return False
    return True


