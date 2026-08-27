"""
100. Same Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q: # If p & q are not null
            if p.val != q.val: # Check the value of the node
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # Then check if the left trees & right trees are same
        if not p and not q: # Base case - If both input trees are null then they are same return Truee
            return True
        return False # 2nd Base case - If one of the trees is null but the other is not
        