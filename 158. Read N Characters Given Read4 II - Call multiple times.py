# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
  buf4 = [""] * 4
  prev_index, prev_len = 0, 0

  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    i = 0
    while i < n:
      if self.prev_index < self.prev_len:
        buf[i] = self.buf4[self.prev_index]
        i += 1
        self.prev_index += 1
      else:
        self.prev_len = read4(self.buf4)
        self.prev_index = 0
        if not self.prev_len:
          break
    return i
