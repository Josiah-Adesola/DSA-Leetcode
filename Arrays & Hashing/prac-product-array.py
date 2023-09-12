def productExceptSelf(nums):
    answer = [1] * (len(nums))
    before = 1
    for i in range(len(nums)):
        answer[i] = before
        before *= nums[i]

    after = 1
    for i in range(len(nums) -1, -1, -1):
        answer[i] *= after
        after *= nums[i]

    return answer
        
        
        
nums = [1,2,3,4]
print(productExceptSelf(nums))