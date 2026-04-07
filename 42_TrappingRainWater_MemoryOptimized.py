class Solution:
    """
    2 Pointer Approach
    This implementation only uses O(1) memory
    Logic:
    [4, 2, 3, 5, 1, 6]
    We start at l->4 & r->6 and max_l -> 4 & max_r -> 6
    If max_l < max_r we increment l
    Then update max_l to be the max of the leftmost elements
    Then calculate result = max_l - height[l]
    Pass 1:
    max_l = 4, max_r = 6
    l = 0, r = 5
    l = 1
    max_l = max(4,2) = 4
    res = 4 - 2 = 2
    With this approach, we are ensuring that for each element,
    the pointers always point to the max values on either side of the particular element
    """
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0
        while l<r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max_r - height[r]
        return res