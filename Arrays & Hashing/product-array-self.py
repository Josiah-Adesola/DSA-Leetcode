def productExceptSelf(nums):
    # build out left product and right product arrays
    left = [nums[0]] # start with most left item aka first item
    right = [nums[-1]] # start with most right item aka last item
    
    # iterate through to create the left and right product arrays
    for i in range(1, len(nums)):
        left.append(left[i-1]*nums[i])
        right.insert(0, nums[len(nums)-1-i]*right[0])

    # append 1 to the right arr to avoid index out of bounds err
    right.append(1)
    
    # building the return list
    ret = [right[1]]
    for i in range(1, len(nums)):
        ret.append(left[i-1]*right[i+1])

    return ret
        
        
        
        
nums = [1,2,3,4]
print(productExceptSelf(nums))

