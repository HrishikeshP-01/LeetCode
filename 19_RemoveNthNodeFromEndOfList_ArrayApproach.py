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
    Array Approach
    One Pass

    Logic:
    During 1 pass we store all nodes in an array - O(n)
    Now for a given position we can easily remove the node - O(1)

    Time Complexity = O(n)
    Memory Complexity = O(n)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 Pass Array Approach
        nodes = []
        c = head
        while c:
            nodes.append(c)
            c = c.next
        curr, prev, nxt = None, None, None
        if len(nodes) - n - 1 >= 0: # Edge case: if curr node is the first node, prev=None
            prev = nodes[len(nodes)-n-1]
        curr = nodes[len(nodes)-n] # We will always have a curr node as per the question
        if len(nodes) - n + 1 < len(nodes):  # Edge case: If curr is the last node, nxt=None
            nxt = nodes[len(nodes)-n+1]
        if prev and nxt: # if curr has nodes before & after it
            prev.next = nxt
        elif prev: # If curr is the last node in the list
            prev.next = None
        elif nxt: # If curr is the first node in the list
            head = nxt
            curr.next = None
        else: # If curr is the only node in the list
            return None
        return head