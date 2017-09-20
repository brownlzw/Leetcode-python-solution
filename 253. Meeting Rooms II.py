# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import heappush, heappop


class Solution(object):
  def minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    # intervals.sort(key = lambda x: x.start)
    # rooms = []
    # count = 0
    # for interval in intervals:
    #   if not rooms or rooms[0] > interval.start:
    #     count += 1
    #   else:
    #     heappop(rooms)
    #   heappush(rooms, interval.end)
    # return count

    if not intervals:
      return 0

    start = sorted([interval.start for interval in intervals])
    end = sorted([interval.end for interval in intervals])

    k = 0
    count = 0
    for i in range(len(start)):
      if start[i] < end[k]:
        count += 1
      else:
        k += 1
    return count