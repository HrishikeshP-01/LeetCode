"""
1. Two Sum
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        HashMap Method
        Iterate through the array
        Check if the target-current number i.e, the needed number
        exists in the hashmap already
        if yes return the current pos & the needed number's position
        if not store the current number & pos in the hashmap

        (In this implementation I store the needed number in the hashmap & search if the current number exists. Just the reverse approach both works)
        """
        indexMap = {}
        for i in range(len(nums)):
            if indexMap.get(nums[i], -1) != -1:
                return [indexMap[nums[i]], i]
            else:
                indexMap[target-nums[i]]=i

####
"""
Using enumerate
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i, n in enumerate(nums):
            if indexMap.get(n, -1) != -1:
                return [indexMap[n], i]
            else:
                indexMap[target-n]=i
"""