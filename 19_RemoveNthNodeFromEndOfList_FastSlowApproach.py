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
    Fast-Slow pointer approach - Still a 2 pass approach (if the node to be removed is before the mid, we have to iterate over it again)
    Time Complexity = O(n)
    Space Complexity = O(1)

    Logic:
    If we use a fast slow pointer to iterate through the array
    At the end of the iteration it the fast pointer points to end of the list
    Slow pointer points to middle of the list
    If we keep a counter for both fast & slow; we can get the position of the tail node as well as the mid node

    Then we calculate which node needs to be removed

    If that node position > mid node we start traversing from the mid node till we reach that element & remove it
    If that node position <= mid node we start traversing from the head till we reach the element & remove it

    How is this O(n) in TC?
    The fast slow pointer iteration runs n/2 times
    Then the traversal to remove the given node runs form n/2 times in the worst case
    Total time taken = n/2 + n/2 = O(n) in the worst case
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 Pass, Fast-Slow pointer approach
        fast, slow = head, head
        end_pos, mid_pos = 0, 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            mid_pos += 1
            end_pos += 2
        if not fast:
            end_pos -= 1
        node_to_remove_pos = end_pos + 1 - n
        start = None
        prev = None
        nxt = None
        counter = 0
        if node_to_remove_pos > mid_pos:
            start = slow
            counter = mid_pos
        else:
            start = head
        # Edge case
        if start.next:
            nxt = start.next

        for i in range(counter, node_to_remove_pos):
            prev = start
            start = start.next
            if start:
                nxt = start.next
        if prev and nxt: # curr node has nodes on either side of it
            prev.next = nxt
        elif prev: # curr node is the last node in the list
            prev.next = None
        elif nxt: # curr node is the first node in the list
            head = nxt
        else: # curr node is the only node in the list
            return None
        return head