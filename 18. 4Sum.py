class Solution(object):
    def fourSum(self, nums, target):
        def findNsum(nums, pos, target, N, result, results):
            if len(nums) - pos < N or N < 2 or target < nums[pos]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = pos,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(pos, len(nums)-N+1):
                    if i == pos or (i > pos and nums[i-1] != nums[i]):
                        findNsum(nums, i + 1, target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), 0, target, 4, [], results)
        return results
