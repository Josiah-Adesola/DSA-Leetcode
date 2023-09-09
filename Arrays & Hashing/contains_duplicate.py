def ContainsDuplicate(num):
    num = sorted(num)
    for i in range(len(num) -1):
        if num[i] == num[i + 1]:
            return True
    return False 

        

nums = [1,2, 3, 1]
print(ContainsDuplicate(nums))