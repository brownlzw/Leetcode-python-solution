# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    pass

class Solution(object):
    def findCelebrity(self, n):
        x = 0
        for i in xrange(1, n):
            if knows(x, i):
                x = i
        for i in xrange(x):
            if knows(x, i):
                return -1
        for i in xrange(x+1, n):
            if not knows(i, x):
                return -1
        return x