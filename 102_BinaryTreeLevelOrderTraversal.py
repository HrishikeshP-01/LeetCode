"""
102. Binary Tree Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Breadth First Search Traversal
    Logic:
    Each level is stored in the deque
    While the deque is non-empty:
        At the start all the nodes in the deque belong to the same level
        For the current lenght of the dequeu:
            Pop each node from the left & if they have valid l & r pointers push them to the right
        At the end of this loop the deque will contain the next level

    The result required for this problem is the values at each level so just store them in a variable & return it
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        d = deque([root])
        while d:
            current_level = []
            for i in range(len(d)):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                current_level.append(node.val)
            levels.append(current_level)
        return levels


        