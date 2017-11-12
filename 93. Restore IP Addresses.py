class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        """
        def dfs(tmp, cnt, cur):
            if len(tmp) > 3 * cnt or len(tmp) < cnt:
                return
            if not cnt:
                res.append(cur)
                return
            for i in xrange(min(3, len(tmp) - cnt + 1)):
                if i == 2 and int(tmp[:3]) > 255:
                    continue
                dfs(tmp[i + 1:], cnt - 1, cur + [tmp[:i + 1]])
                if tmp[0] == '0':
                    break

        res = []
        dfs(s, 4, [])
        return ['.'.join(i) for i in res]
    # O(3 ^ 4), O(12 * 3)