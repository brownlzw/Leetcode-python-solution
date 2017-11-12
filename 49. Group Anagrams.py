class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # O(N * KlogK), K is len(longest str)
    res = []
    if not strs:
      return res
    m = {}
    for s in strs:
      sort_s = "".join(sorted(s))
      if sort_s in m:
        m[sort_s].append(s)
      else:
        m[sort_s] = [s]
    return list(m.values())

    # O(N * K), K is len(longest str)
    ans = collections.defaultdict(list)
    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord('a')] += 1
      ans[tuple(count)].append(s)
    return ans.values()