"""
25. Reverse Nodes in k-Group
Solved
Hard
Topics
premium lock icon
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Logic - 
    Consider the list as being divided into k groups
    Dummy -> A -> B -> C -> D -> E 
    if k = 2
    Dummy -> (A->B) -> (C->D) -> E
    Each group has a prev & next node
    We need to reverse the bucket & point the new start to prev
    and new end to next node
    Dum -> (A -> B) -> C
    while reversing A needs to point to C
    B needs to point to A
    So initialize a variable that points to C first then during iteration gets set to A
    Finally once reversed we need to point Dum -> B
    
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        groupPrev = dummy

        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next

            prev = kthNode.next
            curr = groupPrev.next
            # Reverse between curr & kthNode
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
        return dummy.next

    def getKthNode(self, node:ListNode, k:int):
        while node and k>0:
            node = node.next
            k-=1
        return node