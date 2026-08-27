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
    While using the iterative approach it's easier to do Preordered DFS
    What is Preordered DFS?
    In the recursion method we calculated depth bottom-up. We returned the depth from the bottom, gradually increasing it by 1
    In Preordered DFS we move towards the leaf nodes while increasing depth by 1

    Logic:
    Use a stack for FIFO to get the preordered i.e., the topmost nodes first
    The stack stores both the node as well as the depth so far from the root node till that node
    1. Pop a node from the stack 
    2. If the depth is greater than the max_depth update max_depth
    3. Push the left & right nodes of the popped nodes into the stack with their depths (their depth is the depth of current node + 1)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        depth = 0
        max_depth = 0
        while stack:
            popped, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if popped.left:
                stack.append((popped.left, depth+1))
            if popped.right:
                stack.append((popped.right, depth+1))
        return max_depth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Above logic simplified & more efficient
    Here we don't use the checks used in the above code
    Since We start with max_depth = 0
    if we update max_depth only if the popped node is valid,
    the edge cases we checked for above don't need to be handled:
    1. If root is null - the max depth won't be updated & 0 is returned
    2. popped.left or popped.right is null - they get pushed into the stack but they get popped in due course &
    the max_depth is not updated
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        depth = 0
        max_depth = 0
        while stack:
            popped, depth = stack.pop()
            if popped:
                max_depth = max(max_depth, depth)
                stack.append((popped.left, depth+1))
                stack.append((popped.right, depth+1))
        return max_depth
