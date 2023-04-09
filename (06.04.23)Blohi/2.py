nums = [0,1,0,3,12]




cnt_zeros = 0
# for i in range(len(nums)):
#     if nums[i] ==0:
#         cnt_zeros +=1
#     else:
#         nums[i], nums[i-cnt_zeros] = nums[i-cnt_zeros], nums[i]
# print(nums)
for i in range(len(nums)):
    if nums[i] == 0:
        cnt_zeros +=1
    else:
        nums[i], nums[i-cnt_zeros] = nums[i-cnt_zeros], nums[i]
print(nums)