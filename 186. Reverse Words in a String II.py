class Solution:
  # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
  # @return nothing
  def reverseWords(self, s):
    s.reverse()

    index = 0
    for i in range(len(s)):
      if s[i] == " ":
        s[index: i] = reversed(s[index: i])
        index = i + 1

    s[index:] = reversed(s[index:])
