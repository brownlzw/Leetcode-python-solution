class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            self.twosum(res, nums, i + 1, -nums[i])
        return res

    def twosum(self, res, nums, low, target):
        if nums[low] + nums[low + 1] > target or nums[-2] + nums[-1] < target:
            return
        low, high = low, len(nums) - 1
        while low < high:
            val = nums[low] + nums[high]
            if val == target:
                res.append([-target, nums[low], nums[high]])
                low += 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                high -= 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif val > target:
                high -= 1
            else:
                low += 1

    def threeSum2(self, nums):
        pos, neg = {}, {}
        for num in nums:
            if num > 0:
                if num not in pos:
                    pos[num] = 1
                else:
                    pos[num] += 1
            else:
                if num not in neg:
                    neg[num] = 1
                else:
                    neg[num] += 1

        rst = []
        if 0 in neg and neg[0] > 2:
            rst.append([0, 0, 0])

        for p in pos.keys():
            for n in neg.keys():
                inverse = -(p + n)
                if inverse in pos:
                    if inverse < p or inverse == p and pos[inverse] > 1:
                        rst.append([n, inverse, p])
                elif inverse in neg:
                    if inverse > n or inverse == n and neg[inverse] > 1:
                        rst.append([n, inverse, p])
        return rst
