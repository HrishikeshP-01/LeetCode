"""
543. Diameter of Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
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
    Recursive DFS
    Time Complexity = O(n) n-> number of nodes
    Space Complexity = O(h) n-> height of tree
                     = O(log n) for a balanced tree
                     = O(n) for an unbalanced tree (worst case)
    Logic:
    The diameter of a tree is defined as - length of longest path between any 2 nodes of the tree
    But what is the longest path between 2 nodes in a tree?
    Is the path from the deepest node from left to the deepest node from the right
    Distance of deepest node from left = depth of left subtree
    Distance of deepest node from right = depth of right subtree
    
    For each node from bottom up:
    Calculate the left depth, the right depth
    The longest path at that point is the left depth + right depth
    Depth of that node = 1 + max(left depth + right depth)
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        x, y = self.depth_calc(root, 0)
        return y
        
    def depth_calc(self, root, max_so_far):
        if not root:
            return 0, max_so_far
        left_depth, max_so_far1 = self.depth_calc(root.left, max_so_far)
        right_depth, max_so_far2 = self.depth_calc(root.right, max_so_far)
        max_so_far = max(max_so_far, max_so_far1, max_so_far2, left_depth+right_depth)
        print(max_so_far)
        return 1+max(left_depth,right_depth), max_so_far


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Recursive DFS - Nested function & global variable    
    Same TC & MC
    Same logic but more efficient than above implementation
    We use a global variable to store the diameter
    We use a nested function to easily call it
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def depth(root):
            if not root:
                return 0
            l_depth = depth(root.left)
            r_depth = depth(root.right)
            self.result = max(self.result, l_depth+r_depth)
            return 1+max(l_depth, r_depth)
        
        depth(root)
        return self.result