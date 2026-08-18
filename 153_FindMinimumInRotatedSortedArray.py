"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

class Solution:
    """
    Nature of a perfectly sorted array - Beginning element is always less than the Last element
    A rotated array: The beginning element is guaranteed to be greater than the last element
    While the beginning element l is greater than the ending element u:
        Calculate mid
        If the middle is >= the starting element, that means the greatest element is still somewhere after the middle
        This also means middle is greater than u (because l>u)
        So the least element can't be mid but is somewhere after mid
        So the new l = mid+1
        But if the middle is <= the final element, that means the least element could be mid itself or could be before mid
        so u=mid
    The loop ends when l is no longer greater than the u value, at which stage you'd have found the minimum element

    Demo:
    [2, 1]
    l = 0, u = 1
    2>1:
        mid = 0
        2>=2 so l=mid+1=0+1=1
    1>1: False
    Loop Exits returns 1

    1. In the condition why is > used instead of >=
    Take the case [2 1 2]
    l value = u value doesn't guarantee you found the min. element
    2. Why is l's update l=mid+1 while u's update u=mid?
    Condition is nums[mid]>nums[l] so the min element is guaranteed to be to the right of mid i.e, from mid+1
    Also it keeps us moving forward in the solution space. E.g: [2 3 1]
    l=0, u=2
    1st iteration:
        mid=1
        mid->3
        update l->3, l=1
    2nd iteration:
        l=1, u=2
        mid = 1
        mid->3
        l is already pointing to 3, l=1 no update doesn't proceed to explore the remaining solution space
    """
    def findMin(self, nums: List[int]) -> int:
        l, u = 0, len(nums)-1
        while nums[l]>nums[u]:
            mid = int((l+u)/2)
            if nums[mid] >= nums[l]:
                l = mid+1
            elif nums[mid] <= nums[u]:
                u = mid
        return nums[l]
