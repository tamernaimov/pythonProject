nums = [5,2,7,1,4]
while True:
    is_swithced = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            is_swithced = True
            nums[i], nums[i+1] = nums[i+1], nums[i]

    if is_swithced == False:
        break
    print(nums)

nums = [5, 2, 7, 1, 4]
