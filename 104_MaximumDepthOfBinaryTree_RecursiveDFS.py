"""
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Recursion + Depth First Search approach
    Logic:
    If the current node is null the depth from that point to the leaf node is 0
    Else the depth from that point is the current layer + maximum(depth of left branch, depth of right branch) i.e, 1 + max(depth of l branch, depth of r branch)
    Return the depth
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        return depth + max(l_depth, r_depth)
        