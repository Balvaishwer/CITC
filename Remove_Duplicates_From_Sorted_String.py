class Solution:
    def removeDuplicates(nums)
        if len(nums) == 0:
            return 0
        j = 0
        i = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                j += 1
                nums[j] = nums[i]
        return j + 1



