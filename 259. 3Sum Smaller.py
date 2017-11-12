class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        nums.sort()
        n = len(nums)
        if nums[-1] + nums[-2] + nums[-3] < target:
            return n * (n - 1) * (n - 2) / 6

        cnt = 0
        for i in xrange(len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] >= target:
                break
            if nums[i] + nums[-1] + nums[-2] < target:
                cnt += (n - i - 1) * (n - i - 2) / 2
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] >= target:
                    r -= 1
                else:
                    cnt += r - l
                    l += 1
        return cnt
    # O(n^2), O(1)