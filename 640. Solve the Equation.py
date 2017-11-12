class Solution(object):
    def solveEquation(self, equation):
        k, const = 0, 0
        i = 0
        left = True
        for j, c in enumerate(equation):
            if c in "+-=" and j > i or j == len(equation) - 1:
                if j == len(equation) - 1:
                    j += 1
                sub = equation[i:j]
                if 'x' in sub:
                    v = sub.rstrip('x')
                    if not v or len(v) == 1 and v[0] in "+-":
                        v += '1'
                    v = int(v)
                    if not left:
                        v = -v
                    k += v
                else:
                    v = int(sub)
                    if left:
                        const -= v
                    else:
                        const += v
                i = j
                if c == '=':
                    i += 1
                    left = False
        if k != 0:
            return 'x={}'.format(const / k)
        elif const == 0:
            return 'Infinite solutions'
        else:
            return 'No solution'
