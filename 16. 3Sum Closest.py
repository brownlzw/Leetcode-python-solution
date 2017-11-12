# Basic idea: sort the array, from left and right check
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length <= 3:
            return sum(nums)
        nums = sorted(nums)
        minSum = nums[0] + nums[1] + nums[2]
        # if minimum of the sum greater than target
        if minSum >= target:
            return minSum

        maxSum = nums[-3] + nums[-2] + nums[-1]
        if maxSum <= target:
            return maxSum

        if target - minSum < maxSum - target:
            closest, distance = minSum, target - minSum
        else:
            closest, distance = maxSum, maxSum - target

        for i in range(length - 2):
            # skip if already checked
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, length - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return target
                dis = abs(target - s)

                # if get closer
                if dis < distance:
                    closest, distance = s, dis
                elif s < target:
                    # if max sum of current `left to right` less than target, exit
                    if nums[i] + nums[right] * 2 < target:
                        break
                    left += 1
                else:
                    # if current min sum greater than target, exit
                    if nums[i] + nums[left] * 2 > target:
                        break
                    right -= 1
        return closest