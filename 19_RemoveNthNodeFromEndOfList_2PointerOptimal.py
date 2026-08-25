"""
19. Remove Nth Node From End of List
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    2 Pointer approach
    Most optimal - One Pass solution
    Time Complexity = O(n)
    Memory Complexity = O(1)

    Logic:
    We want to land on an element such that it's exactly n-1 spaces before the last element
    So if we start with 2 pointers: l->head & r->head+(n-1)th node
    And update l & r by 1 place with each iteration till r reaches the last node
    Then l will be pointing to the node that we want to remove

    But to remove it we need to keep track of the node before l, we use l_prev for that
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 pointer approach
        l, r = head, head
        l_prev = None
        for i in range(n-1):
            r = r.next
        # Now l is at the start, r is n steps ahead of l
        while r and r.next:
            r = r.next
            l_prev = l
            l = l.next
        # At the end of the loop r points to the last node in the list
        # l is exactly n paces behind r & is the node to be removed
        if l_prev and l.next: # If there are nodes before & after the node we want to remove
            l_prev.next = l.next
        elif l_prev: # If the node we want to remove is the last node
            l_prev.next=None
        elif l.next: # If the node we want to remove is the first node
            head=l.next
        else: # If the node we want to remove is the only node
            return None
        return head
