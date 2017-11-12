# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            buf4 = ['', '', '', '']
            count = read4(buf4)  # Read file into buf4.
            if not count: break  # EOF
            if n - i < count:
                count = n - i
            buf[i:] = buf4[:count]  # Copy from buf4 to buf.
            i += count
        return i

    # O(n), O(1)
