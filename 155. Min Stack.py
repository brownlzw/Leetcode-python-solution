class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.m = -float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.m:
            self.s.append(self.m)
            self.m = x
        self.s.append(x)

    def pop(self):
        """
        :rtype: void
        """
        top = self.s.pop()
        if top == self.m:
            self.m = self.s.pop()
        return top

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m



    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

    # O(1), O(n)