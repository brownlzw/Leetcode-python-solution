class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = [0 for _ in range(26)]
        for task in  tasks:
            freq[ord(task) - ord('A')] += 1
        most_freq = max(freq)
        cnt = freq.cnt(most_freq)
        res = (most_freq - 1) * (n + 1) + cnt
        if res > len(tasks):
            return res
        else:
            return len(tasks)

    # Can't change sequence
    def leastInterval(self, tasks, n):
        m = {}
        res = 0
        for task in tasks:
            if task in m and m[task] + n + 1 > res:
                res = m[task] + n + 1
            else:
                res += 1
            m[task] = res
        return res

print Solution().leastInterval(["A","D","A","B","B","C"],2)


