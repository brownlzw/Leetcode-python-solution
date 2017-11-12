class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        res = 0
        for d in data:
            if res == 0:
                if d >> 5 == 0b110:
                    res = 1
                elif d >> 4 == 0b1110:
                    res = 2
                elif d >> 3 == 0b11110:
                    res = 3
                elif d >> 7 != 0:
                    return False
            else:
                if d >> 6 != 0b10:
                    return False
                res -= 1
        return res == 0