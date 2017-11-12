# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        s, e = newInterval.start, newInterval.end
        if e < intervals[0].start:
            intervals.insert(0, newInterval)
            return intervals
        if s > intervals[-1].end:
            intervals.append(newInterval)
            return intervals
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        i = len(left)
        j = len(right)
        if i + j != len(intervals):
            s = min(s, intervals[i].start)
            e = max(e, intervals[-j - 1].end)
        return left + [Interval(s, e)] + right

    def insert2(self, i1, i2):
        res = []
        if i1[0].start < i2[0].start:
            s, e = i1[0].start, i1[0].end
            i, j = 1, 0
        else:
            s, e = i2[0].start, i2[0].end
            i, j = 0, 1
        while i < len(i1) or j < len(i2):
            if j == len(i2) or i < len(i1) and i1[i].start <= i2[j].start:
                cur = i1[i]
                i += 1
            else:
                cur = i2[j]
                j += 1
            if cur.start <= e:
                if cur.end > e:
                    e = cur.end
            else:
                res.append(Interval(s, e))
                s, e = cur.start, cur.end
        res.append(Interval(s, e))
        return res

    def insert3(self, i1, i2):
        res = []
        if i1[0].start < i2[0].start:
            e = i1[0].end
            i, j = 1, 0
        else:
            e = i2[0].end
            i, j = 0, 1
        while i < len(i1) or j < len(i2):
            if j == len(i2) or i < len(i1) and i1[i].start <= i2[j].start:
                cur = i1[i]
                i += 1
            else:
                cur = i2[j]
                j += 1
            if cur.start < e:
                cur_s, cur_e = cur.start, min(e, cur.end)
                if res and cur_s < res[-1].end:
                    if cur_e > res[-1].end:
                        res[-1].end = cur_e
                else:
                    res.append(Interval(cur_s, cur_e))
            if cur.end > e:
                e = cur.end
        return res

a = Solution().insert3([Interval(1, 2), Interval(5, 7), Interval(9, 12), Interval(10, 11), Interval(11, 14), Interval(15, 17)], [Interval(6,13),Interval(15,17)])
for i in a:
    print i.start, i.end