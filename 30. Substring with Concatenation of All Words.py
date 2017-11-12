class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length = len(s)
        sw_l, tot = len(words[0]), len(words) * len(words[0])

        ans, cnt = [], {}

        for w in words:
            if w in cnt:
                cnt[w] += 1
            else:
                cnt[w] = 1

        def helper(start):
            cnt2 = {}
            end = start

            while start + tot <= length:
                w = s[end:end + sw_l]
                end += sw_l
                if w not in cnt:
                    start = end
                    cnt2.clear()
                    continue

                if w in cnt2:
                    cnt2[w] += 1
                else:
                    cnt2[w] = 1

                # print cnt2, start, end
                while cnt2[w] > cnt[w]:
                    cnt2[s[start:start + sw_l]] -= 1
                    start += sw_l
                if end - start == tot:
                    ans.append(start)

        for i in range(min(length - tot + 1, sw_l)):
            helper(i)

        return ans