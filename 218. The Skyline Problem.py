from heapq import heappush, heappop

class Solution:
  def getSkyline(self, LRH):
    live = []
    res = []
    i, n = 0, len(LRH)
    while i < n:
      if not live or LRH[i][0] <= -live[0][1]:
        cur = LRH[i][0]
        while i < n and LRH[i][0] == cur:
          heappush(live, (-LRH[i][2], -LRH[i][1]))
          i += 1
      else:
        cur = -live[0][1]
        while live and -live[0][1] <= cur:
          heappop(live)
      h = len(live) and -live[0][0]
      if not res or h != res[-1][1]:
        res += [cur, h],
    return res


