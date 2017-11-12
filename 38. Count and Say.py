class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = [1]
        n -= 1
        while n:
            new = []
            prev, cnt = cur[0], 0
            for i in xrange(1, len(cur) + 1):
                if i != len(cur) and cur[i] == cur[i - 1]:
                    cnt += 1
                else:
                    new.append(cnt)
                    new.append(prev)
                    prev, cnt = cur[i], 1
            cur = new
            n -= 1
        return "".join(map(str, cur))
    # O(n * l), O(l)