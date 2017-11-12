def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    for num in nums:
        if num:
            nums[i] = num
            i += 1
    for j in range(i, len(nums)):
        nums[j] = 0

    # follow up: 不不需要保留留原来数组⾥里里元素的相对位置同时要求对数组写⼊入次数最少（读并不不受限制）。⼀一样是2 pointers解
def moveZeros2(nums):
    i, j  = 0, len(nums) - 1
    while i < j:
        while i < j and nums[i] != 0:
            i += 1
        while i < j and nums[j] == 0:
            j -= 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

moveZeros2([])
