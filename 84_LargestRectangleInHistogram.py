"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution:
    """
    Stack Approach
    Stack holds 2 values - the height & the index from which the rectangle of that height begins
    Iterate over heights
        The current height is to be pushed to the stack by default & the default index from which the rectangle begins is the current index
        But as long as the top most element of the stack is > current height:
            This means that the rectangle of the current height could extend backwards
            At the same time the rectangle of the top's height ends there
            So pop top & calculate the area of the rectangle with top's height, the index from which the rectangle being 
            & current index which is the point where the rectangle ends

            Also since the current height can extend backwards, update the start index of the current height to the start index of the popped entry

        Now we need to push the current height onto the stack with the start index of the current height
    If the stack is still full (the remaining entries are in increasing order of height)
        The area of the rectangle is the height * (end of the histogram - position where that height starts)
    Track the max area & return it
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for pos, h in enumerate(heights):
            top_pos = pos
            while stack and stack[-1][0]>h:
                max_area = max(max_area, stack[-1][0]*(pos-stack[-1][1]))
                top_h, top_pos = stack.pop()

            stack.append([h, top_pos])
            #print(stack)
        while stack:
            top_h, top_pos = stack.pop()
            max_area = max(max_area, top_h*(len(heights)-top_pos))
        return max_area
