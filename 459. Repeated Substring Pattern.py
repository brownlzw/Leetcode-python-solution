class Solution(object):
  def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    news = s * 2
    if s in news[1: -1]:
      return True
    else:
      return False
    """
    First char of input string is first char of repeated substring
    Last char of input string is last char of repeated substring
    Let S1 = S + S (where S in input string)
    Remove 1 and last char of S1. Let this be S2
    If S exists in S2 then return true else false
    Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
    https://discuss.leetcode.com/topic/68206/easy-python-solution-with-explaination

    Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.

    Fine. How do we apply that to this problem? We consider every rotation of string S such that it's rotated by k units [k < len(S)] to the left. Specifically, we're looking at strings "elloworldh", "lloworldhe", "loworldhel", etc...

    If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times), then we can check if the string is equal to some rotation of itself, and if it is, then we know that the string is periodic. Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation of itself for all values of R such that 0 < R < len(S).
    """

    l = len(s)
    for i in xrange(1, l):
      if l % i == 0 and s[:i] * (l / i) == s:
        return True
    return False
