class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        i = carry = 0
        res = []
        while i < len(num1) or i < len(num2) or carry:
            if i < len(num1):
                carry += int(num1[i])
            if i < len(num2):
                carry += int(num2[i])
            res.append(carry % 10)
            carry /= 10
            i += 1
        tmp = []
        for num in res:
            tmp.append(str(num))
        tmp = ''.join(tmp)
        return tmp[::-1]

    # O(max(m, n)), O(max(m, n) + 1)