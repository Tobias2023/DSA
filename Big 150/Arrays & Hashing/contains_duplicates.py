'''
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Approach ideas:

- Set
  - Check id array is empty 
  - init a set
  - pass num values to the set 
  - check if length is the same

'''

def is_duplicates(nums):
  if nums == []:
    return -1

  num_set = set([])

  for i in nums: 
    num_set.add(i)

  if len(num_set) != len(nums):
    return True

  return False

print(is_duplicates([1,1,1,3,3,4,3,2,4,2])) # True
print(is_duplicates([1,2,3,4,5,6,7])) # False 


'''
LeetCode Submission: 
===================

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return -1 
        nums_set = set([])
        for i in nums: 
            nums_set.add(i)
        if len(nums) != len(nums_set):
            return True  
        return False

'''

# 04/11/2022 13:17	Accepted	655 ms	26.1 MB	python3
