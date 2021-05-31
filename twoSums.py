'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

#brute force method.
def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            targetsum = nums[i] + nums[j]
            if targetsum == target:
                return [i,j]


#one pass solution
def twoSumsHash(nums,target):
    seen = {}
    for index, num in enumerate(nums):
        remaining = target - num #eg target = 9, nums = [2,7,...], remaining = 7, 2
        if remaining in seen:
            return [seen[remaining], index] #returns [seen[2] --> returns current index (i.e. the other complementary num)]
        seen[num] = index #if not in seen, add into seen
        print(seen)
    return []
