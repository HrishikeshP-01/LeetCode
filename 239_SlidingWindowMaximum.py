"""
239. Sliding Window Maximum
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

class Solution:
    """
    This type of problem is a Monotonic Decreasing Problem
    Deque Approach 
    Deque - Is a double ended queue where elements can be inserted or delete from both sides
    Logic:
    We need a data structure that holds the elements in decreasing order for a window
    So the maximum possible element for a window will be the first element of the structure
    To do this we use a Deque

    Why use a Deque over a Stack?
    1. We need to remove elements from both ends
        a. When an element is greater than elements at the right end of the deque
        those elements need to be removed & then the element needs to be inserted at the right
        b. When the max. element was the element that just left the window,
        that element needs to be be removed from the left
        Stack would make this difficult to do
    
    Algorithm:
    [1 1 1 3 7 2 2 2], k=3
    In the 1st window [1 1 1] 3 7 2 2 2; Deque -> [1 1 1]
    In the 2nd window: 1 [1 1 3] 7 2 2 2
        Since 1 is leaving & it's the leftmost element of the deque pop it from the left [1 1]
        3 is to be added from the right. Remove all elements that are less than 3 [1 1] 3
        Deque -> [3]
    In the 3rd window: 1 1 [1 3 7] 2 2 2; Deque -> [3]
        7 is added to the right, remove all elements less than 7
        Deque -> [7]
    In the 4th window: 1 1 1 [3 7 2] 2 2; Deque-> [7]
        2 is added to the right, remove all elements less than 2
        Deque -> [7 2]
    In the 5th window: 1 1 1 3 [7 2 2] 2; Deque->[7 2]
        2 is added to the right, remove all elements less than 2
        Deque-> [7 2 2]
    In the 6th window -> 1 1 1 3 7 [2 2 2]; Deque->[7 2 2]
        7 is leaving the window, it's also the leftmost element so popleft [2 2]
        2 is entering from the right, remove all elements less than 2
        Deque->[2 2 2]

    Why a deque?
    We need all the possible highest numbers in decreasing order so that even if the current maximum
    element leaves a window the next maximum is readily available

    In the below solution I'm storing indices instead of numbers
    It'll make poping from left easier (just have to do an = comparison)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque() # Store indices
        i, j = 0,0
        while j<len(nums):
            # Pop smaller values from q 
            while q and nums[j] > nums[q[-1]]:
                q.pop()
            # Then insert j
            q.append(j)
            if j-i+1 == k: # Reached the sliding window size so find result, then slide
                result.append(nums[q[0]])
                i+=1
                if i>q[0]: # If the largest element so far was at the previous ith position remove it from the deque
                    q.popleft()
            j+=1
        return result
            


