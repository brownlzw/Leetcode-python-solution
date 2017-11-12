class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        prev = int(tokens[0])
        for c in tokens[1:]:
            if c == '+':
                prev = s.pop() + prev
            elif c == '-':
                prev = s.pop() - prev
            elif c == '*':
                prev = s.pop() * prev
            elif c == '/':
                prev = s.pop() / prev
            else:
                s.append(prev)
                prev = int(c)
        return prev
