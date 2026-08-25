"""
287. Find the Duplicate Number
Solved
Medium
Topics
premium lock icon
Companies
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

class Solution:
    """
    2 main constraints:
    MC should be O(1)
    TC should be O(n) linear

    Floyd's Cycle Algorithm
    (Different from Floyd's Hare & Tortoise Algorithm)
    Floyd's cycle algorithm is used to find the beginning of a loop in a linked list
    Algorithm:
    Use a fast & slow pointer to detect a loop
    The moment a loop is detected, use a second slow pointer at the start of the list
    Update the 1st slow pointer & 2nd slow pointer by 1
    The node where the both meet will ALWAYS BE THE FIRST NODE OF THE LOOP - LOOP NODE

    Logic:
    Think of this array of numbers as nodes that store the indices to the next node
    [1 3 4 2 2]
    The 0th node -> 1st node
    1 -> 3
    2 -> 4th node
    3 -> 2nd node
    4 -> 2nd node
    Both the 3rd & 4th node points to the 2nd node
    so a loop exits like: 1 -> 3 -> 2 -> 4
                                     <---|
    Above shows the nodes & the connections between them
    It's clear that it's a singly linked list with a loop
    The start of the loop is the node with the most number of incoming connections
    i.e., the most frequent element (since the elements store the connection from current node to target node)
    We can use Floyd's cycle algorithm to find the starting node of the loop

    Remember values in the array correspond to the indices of the connections
    The nodes are actually the indices of the array
    So the starting node's index is the most frequent element
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        second_slow = 0
        while second_slow != slow:
            slow = nums[slow]
            second_slow = nums[second_slow]
        return slow