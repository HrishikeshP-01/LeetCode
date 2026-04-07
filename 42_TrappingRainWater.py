"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

class Solution:
    """
    2 Pointer Approach
    Logic:
    Consider an array [4, 2, 3, 3, 1, 2, 1]
    The water here is stored between 4 & 3 and 3 & 2
    The units of water stored is 2
    We need to know if water is stored at a particular position
    And calculate how much water is stored
    1. How to understand if water is stored at a particular position?
    We need to know where the "wall" is on the left
    and where the "wall" is on the right
    The "wall" needs to be the tallest or it too becomes a candidate for water storage
    To find the tallest walls on either side we can do a forward & backward pass 
    Find the largest number, till that particular element & that is the wall
    2. How to find how much water is stored at a particular position
    Consider this example: [4, 2, 3]
    The 2nd wall is only 3 units tall so that's the max. water capacity
    The middle element is 2 units tall
    So the total water stored is 3-2
    However, water can only be stored if the middle element is lower than the surrounding walls
    e.g: [4,5,3] or [4,3,3] -> No water can be stored
    So if the total water stored is a negative number or 0 that means that position is higher than the walls & water can't be stored there
    """
    def trap(self, height: List[int]) -> int:
        forward_pass = [0] * len(height)
        backward_pass = [0] * len(height)
        max_l, max_r = 0, 0
        for i in range(len(height)):
            j = len(height) - 1 - i
            
            forward_pass[i] = max_l
            max_l = max(max_l, height[i])

            backward_pass[j] = max_r
            max_r = max(max_r, height[j])

        units = 0
        for i in range(len(height)):
            water = min(forward_pass[i], backward_pass[i]) - height[i]
            if water>0:
                units += water
        return units