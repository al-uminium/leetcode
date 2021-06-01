'''
Given an integer array nums, return true if any value appears at least twice in the array, and return
false if every element is distinct.
'''
# convert to set
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# using hash table
def containsDuplicate(nums):
    duplicate = {}
    for i in range(0,len(nums)):
        if nums[i] in duplicate:
            return True
        else:
            duplicate[nums[i]] = i
    return False