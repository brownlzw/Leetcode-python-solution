class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 2: return 0
        stack = []
        leftmost = -1
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # case ')'
                if not stack: # not valid parenthesis, update leftmost
                    leftmost = i
                else:
                    stack.pop()
                    if not stack: # stack is empty, length is i - leftmost
                        res = max(res, i - leftmost)
                    else: # otherwise, length is i - last index of stack
                        res = max(res, i - stack[-1])
        return res