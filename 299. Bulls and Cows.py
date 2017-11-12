class Solution(object):
  def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    bulls, cows = 0, 0
    m = {}
    for c in secret:
      if c not in m:
        m[c] = 1
      else:
        m[c] += 1
    for i, c in enumerate(guess):
      if c == secret[i]:
        bulls += 1
        m[c] -= 1
    for i, c in enumerate(guess):
      if c != secret[i] and c in m and m[c]:
        cows += 1
        m[c] -= 1
    return str(bulls) + 'A' + str(cows) + 'B'