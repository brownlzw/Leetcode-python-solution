class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        i = 1
        max_digit, max_index = num % 10, 1
        from_digit, from_index = 0, -1
        to_digit, to_index = 0, -1
        temp = num
        while temp > 0:
            cur = temp % 10
            if max_digit > cur:
                from_digit, from_index = max_digit, max_index
                to_digit, to_index = cur, i
            elif max_digit < cur:
                max_digit, max_index = cur, i
            i *= 10
            temp /= 10
        if to_index != -1:
            return num + (from_digit - to_digit) * (to_index - from_index)
        return num
