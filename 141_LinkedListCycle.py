"""
141. Linked List Cycle
Solved
Easy
Topics
premium lock icon
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Floyd's Tortoise & Hare Algorithm
    Approach:
    2 pointers - slow pointer & fast pointer
    Slow pointer moves 1 pace every iteration
    Fast pointer moves 2 paces every iteration
    If fast pointer meets slow pointer, loop exits else it doesn't exist

    Why is it guaranteed that fast pointer will meet the slow pointer?
    Let's say that a loop exists & the distance between fast & slow pointers are x 
    Slow pointer moves away from fast by 1 pace
    Fast pointer moves toward slow by 2 paces
    So every iteration the distance = x + 1 -2 = x-1
    Which eventually converges to 0
    
    Why does this take linear time O(n)?
    In the worst case scenario: The whole list is a loop
    So maximum possible length of the loop is going to be n
    Slow will be at 1 while fast will be at 2 & within n iterations fast will catch up to slow

    Now in the best case scenario, the list isn't a loop
    In which case fast reaches the end within n-1 iterations
    Hence Time Complexity is linear O(n)

    What other approaches can be used?
    We could use a Hashset Approach. Since ListNode is an object, it can be hashed
    But Space Complexity would be O(n) 
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit, tortorise = head, head
        # Why check rabbit as well? Edge case: the list is empty
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tortorise = tortorise.next
            if rabbit == tortorise:
                return True
        return False
        