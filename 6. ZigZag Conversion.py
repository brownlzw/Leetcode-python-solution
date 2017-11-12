class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = []
        n = numRows
        l = 2 * n - 2
        cur_l = l
        for i in xrange(n):
            cur = i
            while cur < len(s):
                res.append(s[cur])
                if 0 < cur_l < l and cur + cur_l < len(s):
                    res.append(s[cur + cur_l])
                cur += l
            cur_l -= 2
        return ''.join(res)

