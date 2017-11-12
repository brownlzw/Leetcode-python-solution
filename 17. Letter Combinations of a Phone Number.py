class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = ['']
        for c in digits:
            res = [i + j for i in res for j in kvmaps[c]]
        return res

        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])  # reduce
