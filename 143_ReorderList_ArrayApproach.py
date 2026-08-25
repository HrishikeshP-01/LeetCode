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
    Array + 2 pointer approach 
    Time Complexity = O(n) + O(n)
    Space complexity = O(n)

    Logic:
    1. Store all nodes in an array
    2. Use 2 pointers one from left of array & one from right
    3. Change the pointer of each node as per the given question
    4. For the middle node (in case of odd) or the n/2 th node (in case of even) set the next ptr to null
    since this is going to be the last node of the reordered list
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        while head:
            arr.append(head)
            head = head.next
        i, j = 0, len(arr)-1
        while i<=j:
            n = arr[i].next
            arr[i].next = arr[j]
            arr[j].next = n
            # The last node, first part only satsifies if it's odd, 2nd part only satisfies if it's even
            if i==j or i+1==j:
                arr[j].next=None
            i+=1
            j-=1

        