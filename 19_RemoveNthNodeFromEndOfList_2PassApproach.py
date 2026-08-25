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
    2 Pass Approach 

    Logic:
    During the first pass we count the number of nodes in the list
    Then we find the position of the node to be removed
    In the second pass we get to the node & remove it

    Time Complexity = O(n) + O(n)
    Memory Complexity = O(1)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 Pass method
        node_count = 0
        p = head
        while p:
            p = p.next
            node_count += 1
        node_pos = node_count - n
        print(node_pos)
        p = head
        for i in range(node_pos-1):
            p = p.next
        if p == head and node_pos==0: # Edge case - if p is the head & the node to be removed is the head node
            if not p.next: # Edge case - if the node to be removed is the head node & it's the only node in the list
                return None
            else: # if node to be removed is the head, & there are other nodes in the list
                head = p.next
        elif p.next:
            c = p.next
            p.next = c.next
            c.next = None
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Same as above but edge cases are easier to understand & handle
    (the if curr: is redundant?)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 Pass method
        node_count = 0
        p = head
        while p:
            p = p.next
            node_count += 1
        node_pos = node_count - n
        prev = None
        curr = head
        print(node_pos)
        for i in range(node_pos):
            prev = curr
            curr = curr.next
        if curr:
            if curr.next and prev:
                prev.next = curr.next
                curr.next = None
            elif prev:
                prev.next = None
            elif curr:
                return curr.next
            else:
                return None
        return head