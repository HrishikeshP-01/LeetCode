"""
2. Add Two Numbers
Solved
Medium
Topics
premium lock icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Standard Linked List Problem
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        dummy = ListNode(0) # It's easier to have a dummy node instead of having to initialize prev nodes, head etc. using branches inside the logic
        l3, prev_l3, head = dummy, dummy, dummy
        while l1 and l2:
            prev_l3 = l3
            l3 = ListNode((l1.val+l2.val+carry_over)%10, None)
            prev_l3.next = l3
            carry_over = int((l1.val+l2.val+carry_over)/10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            prev_l3 = l3
            l3 = ListNode((l1.val+carry_over)%10, None)
            prev_l3.next = l3
            carry_over = int((l1.val+carry_over)/10)
            l1 = l1.next
        while l2:
            prev_l3 = l3
            l3 = ListNode((l2.val+carry_over)%10, None)
            prev_l3.next = l3
            carry_over = int((l2.val+carry_over)/10)
            l2 = l2.next
        if carry_over > 0: # Edge Case: example 9+8=17 if carry_over is still remaining we need to create a new node & add it to the list
            prev_l3 = l3
            l3 = ListNode(carry_over, None)
            prev_l3.next=l3
        return head.next # head is pointing to the dummy node, the actual head is head.next
        