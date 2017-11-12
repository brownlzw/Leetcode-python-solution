from heapq import heappush, heappop
from random import randint


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pq = []
        # i = 0
        # for num in nums:
        #   heappush(pq, num)
        #   if i >= k:
        #     heappop(pq)
        #   i += 1
        # return heappop(pq)
        # O(klogk), O(k)
        def partition(l, r):
            ri = randint(l, r)
            nums[r], nums[ri] = nums[ri], nums[r]
            pivot = nums[r]
            for i in xrange(l, r + 1):
                if nums[i] >= pivot:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
            return l - 1

        l, r = 0, len(nums) - 1
        while True:
            index = partition(l, r)
            if index > k - 1:
                r = index - 1
            elif index < k - 1:
                l = index + 1
            return nums[index]
    # O(n)