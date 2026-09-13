"""
98. Validate Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Logic:
    Node value of a valid BST must be greater than all Left Sub Tree
    and must be less than the Right Sub Tree

    Perform a Depth First Search Traversal but keep track of the 
    maximum & minimum possible values a node can have
    The maximum value a node can have gets updated with each left movement
    The minimum value a node can have gets updated with each right movement
    Initially at the root there is no max. or min. values

    LESSON LEARNT
    If you are doing a null check for non-object variables best use is not None EXPLICITLY
    Eg: is not X 
    Returns False when x=None and x=0
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidNode(node, minVal, maxVal):
            if not node:
                return True
            if minVal is not None and node.val <= minVal: # IMP: Use is not None
                return False
            if maxVal is not None and node.val >= maxVal:
                return False
            l_ok = isValidNode(node.left, minVal, node.val)
            r_ok = isValidNode(node.right, node.val, maxVal)
            return l_ok and r_ok
        return isValidNode(root, None, None)