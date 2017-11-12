class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return 0
        n1, n2 = len(num1), len(num2)
        res = [0 for _ in xrange(n1 + n2)]
        for i in xrange(n2):
            d1, carry = int(num2[n2 - i - 1]), 0
            if not d1:
                continue
            for j in xrange(n1):
                d2 = int(num1[n1 - j - 1])
                res[i + j] += d1 * d2 + carry
                carry = res[i + j] / 10
                res[i + j] = res[i + j] % 10
            res[i + n1] += carry
        i = len(res) - 1
        while i and not res[i]:
            i -= 1
        s = ""
        while i >= 0:
            s += str(res[i])
            i -= 1
        return s
    # O(n1 * n2), O(n1 + n2)