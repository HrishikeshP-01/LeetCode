"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use the Hash Approach
        # Create a hashset, check if the num is in haset if yes return True
        # Else add the number
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False

        # Fastest approach is to just add all numbers into hashset first
        # The check if lenght of hashset is equal to lenght of the array
        # if len(hashset(nums)) == len(nums)