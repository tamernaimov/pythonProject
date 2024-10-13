nums = [5,2,7,1,4]
while True:
    for i in range(len(nums)):
        if nums[i] > nums[i+1]:
            nums[i] = nums[i+1]
    print(nums)
