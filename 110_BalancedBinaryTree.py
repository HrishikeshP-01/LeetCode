"""
110. Balanced Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Recursive DFS
    For each node we need to check if it's balanced at that node or not
    For a Tree to be balanced:
        The left depth & right depth difference should not be greater than 1
        AND
        All the nodes below it should be balanced
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth, balanced = self.findDepth(root, True)
        return balanced

    def findDepth(self, root:TreeNode, balanced: bool):
        if not root and balanced:
            return 0, True
        l_depth, x = self.findDepth(root.left, balanced)
        r_depth, y = self.findDepth(root.right, balanced)
        balanced = x and y
        if abs(l_depth-r_depth) > 1:
            balanced = False 
        return 1 + max(l_depth, r_depth), balanced
        