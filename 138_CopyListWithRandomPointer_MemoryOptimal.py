"""
138. Copy List with Random Pointer
Solved
Medium
Topics
premium lock icon
Companies
Hint
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    O(1) Memory Approach
    Logic:
    Say we have a list A->B->C->D
    We traverse the list, for each node create a copy & add it immediately after the current node
    A->a->B->b->C->c->D->d
    During this pass we only set the value, we can't add the next & random pointers since those nodes haven't been initialized yet
    In the second pass, since we have all the copied nodes initialized we can set the next & random ptr values
    next is the node 2 places ahead of the current node
    random node of the copied node is the node 1 place ahead of the random node of the orginal node
    Eg:
    A->a->B->b
    a.next = a.next.next
    a.random = A.random.next
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Traverse the list & insert copied node just after the current node
        curr = head
        while curr:
            cop = Node(curr.val, None, None)
            cop.next = curr.next
            curr.next = cop
            curr = curr.next.next
        # Traverse the list, set proper next & random values
        new_head = head.next
        curr = head
        while curr:
            cop = curr.next
            next_node = curr.next.next
            if next_node:
                cop.next = next_node.next
            if curr.random:
                cop.random = curr.random.next
            curr = next_node
        return new_head

        