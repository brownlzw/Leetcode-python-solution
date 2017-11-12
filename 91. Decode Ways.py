class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        n = len(s)
        x1, x2, cur = 1, 1, 1
        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] in "12":
                    cur = x1
                else:
                    return 0
            else:
                cur = x2
                if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] in "123456"):
                    cur += x1
            x1 = x2
            x2 = cur
        return cur

        if not s:
            return 0
        mod = 10 ** 9 + 7
        # e0 means # upto cur pos, e1 means # of encode end with 1, e2 means # of encode end with 2
        e0, e1, e2 = 1, 0, 0
        for n in s:
            delta = ord(n) - ord('0')
            # if cur pos 0, then 0
            p0 = 0 if delta == 0 else 1
            # 1? always 1
            p1 = 1
            # 2? 1 if ? < 7
            p2 = 1 if delta < 7 else 0
            # Sum ?, 1?, 2?
            f0 = p0 * e0 + p1 * e1 + p2 * e2
            # if ? == 1 ,then for next pos, ...1 = e0
            f1 = e0 if delta == 1 else 0
            f2 = e0 if delta == 2 else 0
            e0, e1, e2 = f0 % mod, f1, f2
        return e0
