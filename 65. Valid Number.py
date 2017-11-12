class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = False
        numAfterE = True #e后面必须有数字，否则错 这个就是判断有没有
        dot = False
        exp = False
        s = s.strip() # remove spaces for both end
        for i in xrange(len(s)):
            if s[i] == ' ':
                return False # no space in the midlle
            elif s[i] == '+' or s[i] == '-':
                if i > 0 and s[i-1] != 'e': # if not after 'e'
                    return False
            elif s[i].isdigit():
                num = True
                numAfterE = True
            elif s[i] == '.':
                if dot or exp: # '.' or e appeard before
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or not num: # e appeared before or no number before it
                    return False
                exp = True
                numAfterE = False
            else:
                return False # other char
        return num and numAfterE
    # O(n), O(1)