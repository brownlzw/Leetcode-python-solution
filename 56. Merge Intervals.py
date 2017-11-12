# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda i: i.start)
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start <= res[-1].end:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)
        return res
    # O(n), O(1)
