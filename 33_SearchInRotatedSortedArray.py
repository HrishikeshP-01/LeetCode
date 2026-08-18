"""
33. Search in Rotated Sorted Array
Solved
Medium
Topics
premium lock icon
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

class Solution:
    """
    Binary Search Approach
    Instead of a sorted array where the right half of mid is greater & left half is lesser
    Think of the mid as giving rise to 2 possibilities:
    1. The left half could be in increasing order. For example: [3 4 5 1 2]
    Mid is 5 & the left half is in increasing order 3 4 5
    So if mid > l then it's in increasing order
    The number you are searching for could be in this half if:
    target < mid
    target >= l
    In which case we update r = mid-1
    Else the number could be in the other half, l=mid+1
    2. Second possiblitiy is that left half could be contain numbers greater than mid 
    as well as numbers less than mid
    eg: [7 0 1 2 3]
    Left half: 7 0 1
    So if target < mid or target >= l, r=mid-1 search the left half
    Else the target is going to be less than l but greater than mid so search the right, l=mid+1
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = int((l+r)/2)
            if target==nums[mid]:
                return mid
            elif nums[mid]>=nums[l]:
                if target<nums[mid] and target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target<nums[mid] or target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
        return -1