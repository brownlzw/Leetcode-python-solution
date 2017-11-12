class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = {n: ['']}
        wordDict = set(wordDict)
        len_w = set(len(w) for w in wordDict)
        return self.dfs(dp, s, wordDict, 0, len_w)

    def dfs(self, dp, s, wordDict, i, len_w):
        if i not in dp:
            res = []
            for l in len_w:
                if s[i: i + l] in wordDict:
                    for str in self.dfs(dp, s, wordDict, i + l, len_w):
                        res.append(s[i:i + l] + (str and " " + str))
            dp[i] = res
        return dp[i]
    # O(2^n),


        # def wordBreak2(self, s, wordDict):
        #   n = len(s)
        #   dp = {n: n}
        #   wordDict = set(wordDict)
        #   len_w = set(len(w) for w in wordDict)
        #   end = self.dfs2(dp, s, wordDict, 0, len_w)
        #   res = []
        #   i = 0
        #   while i != end:
        #     res.append(s[i:end])
        #     i, end = end, dp[end]
        #   return ' '.join(res)
        #
        #
        # def dfs2(self, dp, s, words, i, len_w):
        #   if i not in dp:
        #     dp[i] = -1
        #     for l in len_w:
        #       if s[i:i + l] in words and self.dfs2(dp, s, words, i + l, len_w) != -1:
        #         dp[i] = i + l
        #         break
        #   return dp[i]
