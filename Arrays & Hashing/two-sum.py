def twoSum(nums, target):
    new_dict = {}
    for i, num in enumerate(nums):
        rem = target - num
        if rem in new_dict:
            return [new_dict[rem], i]
        new_dict[num] = i

    
    
nums = [2, 7, 11, 15]
target = 22
print(twoSum(nums, target))


