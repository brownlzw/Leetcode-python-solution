from collections import defaultdict
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        m = defaultdict(int)
        st = [m]
        atom, num = '', 0
        flag = False
        for i, c in enumerate(formula):
            if flag and (c in '()' or str.isupper(c) or i == len(formula) - 1):
                tmp = st[-1]
                if len(st) != 1:
                    st.pop()
                    m = st[-1]
                for k in tmp.keys():
                    m[k] += tmp[k] * num
                flag = False
            if atom and (str.isupper(c) or c in '()' or i == len(formula) - 1):
                num = num or 1
                m[atom] += num
                atom, num = '', 0
            if c == ')':
                flag = True
                atom, num = '', 0
            elif str.isdigit(c):
                num = num * 10 + int(c)
            elif str.isalpha(c):
                atom += c
            elif i and c == '(':
                m = defaultdict(int)
                st.append(m)
        num = num or 1
        m = st.pop()
        cnt = sorted([(i, m[i]) for i in m.keys()])
        res = ''
        for atom, num in cnt:
            if cnt == 1:
                res += atom
            else:
                res += atom + str(num)
        return res