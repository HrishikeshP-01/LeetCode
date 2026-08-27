"""
235. Lowest Common Ancestor of a Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    This is a Binary Search Tree (BST)
    The left node val is less than parent
    Right node val is greater than parent

    Logic:
        If p >= parent but q <= parent or vice versa then p & q can't exist in the same sub tree
        Each one exists on either side of the parent
        So the least common ancestor is the parent

        Else:
            If both p & q are less than parent they exist on the left subtree, a common ancestor at a level lower than parent exists
            If both p & q are greater than parent they exist on the right subtree, a common ancestor at a level lower than parent exists
    
        Why >= or <=?
        If p or q or both are the same as the root node. Then that is the least common ancestor as no node below it can still have root node
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if (p.val >= root.val and q.val <= root.val) or (p.val <= root.val and q.val >= root.val):
            return root
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Iterative approach 
    Same logic as above (but this implementation is faster since I had a better idea of the logic now)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr