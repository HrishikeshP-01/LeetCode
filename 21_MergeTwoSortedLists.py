"""
21. Merge Two Sorted Lists
Solved
Easy
Topics
premium lock icon
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # This case is not really needed since we are returning the next node of the dummy node
        # So if both lists are empty we get None anyways
        if not list1 and not list2:
            return None
        # The very first head is a dummy node since we don't know where to start
        list3 = ListNode()
        head = list3
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            else:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
        while list1:
            list3.next = list1
            list3 = list3.next
            list1 = list1.next
        while list2:
            list3.next = list2
            list3 = list3.next
            list2 = list2.next
        # Current head is a dummy node so we get the next node for the actual sorted result
        head = head.next
        return head