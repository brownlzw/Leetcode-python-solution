class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return [m[target - num], i]
            m[num] = i

        # 如果有重复值，要求输出所有值⼀一样但是index不不⼀一样
        from collections import defaultdict
        m = defaultdict(list)
        for i, num in enumerate(nums):
            m[num].append(i)
        for i, num in enumerate(nums):
            if target - num in m:
            # 注意 target - num 和 num 一样的情况下怎么处理
                pass
