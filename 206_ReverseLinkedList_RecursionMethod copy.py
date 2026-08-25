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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Recursion method but here I just implemented the iterative method as a recursive fn in a new method
    Time Complexity = O(n)
    Memory Complexity = O(n)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = self.switch(head, None, None)
        return end
        
    def switch(self, head, end, n):
        if not head:
            return end
        n = head.next
        head.next = end
        end = head
        head = n
        return self.switch(head, end,n)

class Solution:
    """
    Recursion method but here it's the same function
    Time Complexity = O(n)
    Memory Complexity = O(n)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

            