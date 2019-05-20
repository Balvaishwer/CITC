def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] not in dict:
            dict[nums[i]] = i
        else:
            return [dict[target - nums[i]], i]
def main():
    nums = [2, 5, 11, 15]
    print(twoSum(nums, 13))


main()