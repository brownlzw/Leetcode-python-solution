class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    def word_search(dp, s, pos, words):
      if pos == len(s):
        return True
      if pos in dp:
        return dp[pos]
      dp[pos] = False
      for i in xrange(pos, len(s)):
        if s[pos:i + 1] in words and word_search(dp, s, i + 1, words):
          dp[pos] = True
          break
      return dp[pos]

    dp = {}
    w_set = set(wordDict)
    return word_search(dp, s, 0, w_set)

  # def wordBreak(self, s, wordDict):
  #   """
  #   :type s: str
  #   :type wordDict: List[str]
  #   :rtype: bool
  #   """
  #   dic = {}
  #   for word in wordDict:
  #     if not len(word) in dic:
  #       dic[len(word)] = Set()
  #     dic[len(word)].add(word)
  #   dp = {}
  #   self.isValid(s, 0, dic, dp)
  #   return dp[0]
  #
  # def isValid(self, s, index, dic, dp):
  #   if index == len(s):
  #     return True
  #   if index in dp:
  #     return dp[index]
  #   for key, wordSet in dic.iteritems():
  #     if key > len(s) - index:
  #       continue
  #     if s[index:index + key] in wordSet and self.isValid(s, index + key, dic, dp):
  #       dp[index] = True
  #       return True
  #   dp[index] = False
  #   return False