"""
230. Kth Smallest Element in a BST
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Algorithm: Inorder Traversal - Recursive Approach
    The inorder traversal of a Binary Search Tree gives the elements in ascending order

    How to perform inorder traversal?
    If a left node exists, go towards the left & apply the same check
    If no left node exists add the current node to the inorder list
    If right node exists, go twards the right & apply check 1

    Perform inorder traversal & store the results in an array, the kth element is the kth smallest element
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def fillInorder(root, l):
            if root.left:
                fillInorder(root.left, l)
            l.append(root)
            if root.right:
                fillInorder(root.right, l)
        if not root:
            return 0
        inorder_list = []
        fillInorder(root, inorder_list)
        return inorder_list[k-1].val