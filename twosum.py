def twosum(nums,target):
    #nums=int []
    #target=int
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[j]+nums[k] ==target:
                return True
    return False
