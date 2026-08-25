"""
143. Reorder List
Solved
Medium
Topics
premium lock icon
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Memory Complexity = O(1)
    Merge Approach
    
    Logic:
    For array: 1 2 3 4 5 6 7
    We can split the array into 2 - [1 2 3 4] & [5 6 7]
    Now we can take an element from the left of 1st array & element from right of 2nd array to get
    1 7 2 6 3 5 4
    But how do we get elements of the 2nd array from the right? It's a singly-linked list?
    We can reverse this list to: [1 2 3 4] & [7 6 5]
    Then we can use the head pointer to get one element from each array in the order we want

    How do we get the middle element (if node count is odd) or n/2th element (if node count is even)?
    We can use a slow & fast pointer.
    Slow updates by 1, fast by 2
    By the time the fast pointer reaches the end of the list, the slow will be pointing to the middle / n/2th element

    Algorithm:
    1. Use slow & fast pointers to split the list
    2. Reverse the 2nd list
    3. Set the pointers as per the desired output
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        # s in now the middle element if there are odd nodes or n/2 th element if there are even nodes
        # so s is the last element of the reordered list
        p = s.next
        s.next = None
        # reverse list starting at p
        p_start = None
        while p:
            n = p.next
            p.next = p_start
            p_start = p
            p = n
        # p_start now points to the reveresed 2nd half of the list
        while p_start:
            next_rev = p_start.next
            next_start = head.next
            head.next = p_start
            p_start.next = next_start
            head = next_start
            p_start = next_rev