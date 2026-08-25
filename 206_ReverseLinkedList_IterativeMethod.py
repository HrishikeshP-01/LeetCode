"""
206. Reverse Linked List
Solved
Easy
Topics
premium lock icon
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Iterative Method
    Logic:
    End node at the beginning is going to be null
    The next node is going to be the new head
    The current node should now point to end
    The new end node is going to be the current node
    The head node is going to be the next node

    At the end of the loop end will point to the new head of the list

    Time Complexity = O(n)
    Memory Complexity = O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = None
        while head:
            next = head.next
            head.next = end
            end = head
            head = next
        return end

