"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Set Approach (Hashmap)
        Optimized Prefix-Postfix approach
        Instead of having seperate prefix & postfix arrays that increase memory complexity
        We just have a single result array
        We store the prefix & postfix values in a variable & use them instead

        In the first pass we compute the prefix & store those values in the result_arr
        In the second pass we compute the postfix & multiply those values with the existing prefix values in result_arr

        The memory used is much lesser
        """
        result_arr = [1]*len(nums)
        prefix = 1
        for i in range(1, len(nums), 1):
            prefix *= nums[i-1]
            result_arr[i] = prefix
        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]
            result_arr[i] *= postfix
        return result_arr