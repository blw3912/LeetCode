nums1 = [0,1]
nums2 = [5,10]

nums = (nums1 + nums2)
nums.sort()
print(nums)

# odd
if len(nums) % 2 == 1:
    posit1 = (len(nums) + 1) / 2 -1
    print(nums[posit1])
else:
    posit1 = len(nums) / 2 -1
    med = (nums[posit1] + nums[posit1 + 1]) / 2
    print(med)