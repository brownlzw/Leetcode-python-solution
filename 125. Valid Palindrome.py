class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
      return True

    s1 = filter(str.isalnum, str(s)).lower()
    return s1 == s1[::-1]

    sn = s.encode('utf-8').translate(None, string.punctuation + ' ').lower()
    return sn == sn[::-1]

    li = [i for i in s.lower() if 'a' <= i <= 'z' or '0' <= i <= '9']
    i, j = 0, len(li) - 1
    while i < j:
      if li[i] != li[j]:
        return False
      i += 1
      j -= 1
    return True

