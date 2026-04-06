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
        Division approach:
        Easiest solution is to find the product of all elements of the array
        Then divide the product by the value of each element
        But they have asked us not to use division operator
        
        Prefix-Postfix approach
        Prefix_arr: Each element in an arry is the product of all numbers before that  particular index in the original array
        Posfix_arr: Each element in an arry is the product of all numbers after that  particular index in the original array
        The result_arr: The product of all numbers except an element can be obtained by multiplying the value of the prefix_arr with the value of the postfix arr at that index
        E.g:
        input_arr = [1, 2, 3, 4]
        prefix_arr = [1, 1, 2, 6]
        postfix_arr = [24, 12, 4, 1]
        result_arr = [24, 12, 8, 6]
        """
        prefix_arr = [1]*len(nums) # The prefix value of the first element needs to be 1 by default
        postfix_arr = [1]*len(nums) # The prefix value of the last element needs to be 1 by default
        result_arr = [1]*len(nums)

        for i in range(1, len(nums), 1): # Start from the second element till the last element since first element doesn't have a prefix
            prefix_arr[i] = prefix_arr[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1): # Start from the second last element till the first element (index 0) since last element doesn't have a postfix
            postfix_arr[i] = postfix_arr[i+1]*nums[i+1]
        print(prefix_arr)
        print(postfix_arr)
        for i in range(len(nums)):
            result_arr[i] = prefix_arr[i]*postfix_arr[i]
        return result_arr