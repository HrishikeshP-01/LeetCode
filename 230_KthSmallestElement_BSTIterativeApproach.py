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
    Inorder Traversal - Iterative Approach

    We need to traverse the Binary Search Tree iteratively:
    Keep an inorder array to get the elements in ascending order
    1. If a left node is present add it to the array
    2. Then check the left node
    3. If no left node is present we need to come back to the parent node
    We keep a stack to keep track of parent nodes
    4. Add the parent node ot the array
    5. If a right node is present add it to the array
    (Repeat the left-right process)
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        stack = [root]
        inorder_arr = []
        while stack and len(inorder_arr)<k: # Optimization since we need the kth smallest element 
        # We only have to do this till k elements are added
            node = stack[-1]
            if node.left and node.left.val not in inorder_arr:
                # Val not in arr condition is added to prevent the left nodes to get added
                # Again after the stack pops the parent node
                # We must ensure that it no longer checks the left & directly appends the parent 
                # to the inorder array
                stack.append(node.left)
                continue
            stack.pop(-1)
            inorder_arr.append(node.val)
            #print(inorder_arr)
            if node.right:
                stack.append(node.right)
                continue
        return inorder_arr[-1]
        