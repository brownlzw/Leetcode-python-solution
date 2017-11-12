class Solution(object):
    def minDistance(self, word1, word2):
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [0 for _ in xrange(l2)]
        for j in xrange(l2):
            pre[j] = j
        for i in xrange(1, l1):
            cur = [i] * l2
            for j in xrange(1, l2):
                cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]
        return pre[-1]
