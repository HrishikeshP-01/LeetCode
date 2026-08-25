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

class Solution:
    """
    Hashmap approach
    Time Complexity = O(n) + O(n)=O(n)
    Memory Complexity = O(n)

    Logic:
    In the first pass map old nodes to new nodes in the hashmap, no need to worry about the links (next & random) 
    since we need all the new nodes initialized before we can create links

    In the second pass fill the links by accessing the relavant node from the hashmap
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case - If the list is empty return none
        if not head:
            return None 
        # In the first pass, map nodes of original list to nodes of new list
        # Only the value is needed now, no need to bother about next & random 
        # as we need all the nodes in the hashmap before we can do that
        d = {}
        curr = head
        while curr:
            nn = Node(curr.val, None, None)
            d[curr] = nn
            curr = curr.next
        # In the second pass, fill the links of the new list
        curr = head
        while curr:
            if curr.next: # Edge case - last node doesn't have a next curr.next will fail
                d[curr].next = d[curr.next]
            if curr.random: # Edge case - some nodes have None as random curr.random will fail
                d[curr].random = d[curr.random]
            curr = curr.next
        return d[head]