"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

class Solution:
    """
    2 Pointer Approach

    [8 7 2 1]
    We start at l -> 8 & r -> 1 & max_area = 0
    The height of the container is the min value = 1
    The width is the difference between the indices = 3 - 0 = 3
    Area = h*w = 1* 3 = 3 
    If area is greater than max_area, update it
    If l < r then increment l
    Else decrement r. This will cover cases like r < l & r == l
    The goal here is we need to be able to traverse the array 
    from either sides towards the center
    to find all possible area combinations 
    """
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        while i<j:
            container_h = min(height[i], height[j])
            container_w = j - i
            area = container_h * container_w
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area