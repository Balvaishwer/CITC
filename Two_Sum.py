def twoSum(nums, target):
    print(nums, target)
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            print("res", nums[i], nums[j], nums[i] + nums[j])
            if nums[i] + nums[j] == target:
                return i, j
def main():
    nums = [3,2,3]
    print(twoSum(nums, 6))


main()