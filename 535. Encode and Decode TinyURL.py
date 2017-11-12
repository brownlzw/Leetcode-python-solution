class Codec:
  count = 0
  low = "abcdefghijklmnopqrstuvwxyz"
  up = low.upper()
  m = {}
  def encode(self, longUrl):
    """Encodes a URL to a shortened URL.

    :type longUrl: str
    :rtype: str
    """
    li = []
    cur = self.count
    while cur:
      i = cur % 53
      if i < 10:
        li.append(str(i))
      elif i < 36:
        li.append(self.low[i - 10])
      else:
        li.append(self.up[i - 36])
      cur /= 53
    s = ''.join(li)
    self.m[s] = longUrl
    return "http://tinyurl.com/" + ''.join(li)


  def decode(self, shortUrl):
    """Decodes a shortened URL to its original URL.

    :type shortUrl: str
    :rtype: str
    """
    return self.m[shortUrl[19:]]



    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(url))