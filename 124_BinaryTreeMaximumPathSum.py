"""
124. Binary Tree Maximum Path Sum
Solved
Hard
Topics
premium lock icon
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
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
    Recursive Depth First Search Approach

    Consider a Tree:
     3
     |
     5
    / \
    8  9
    Paths can exist from each node & it can be of 4 types:
    1. Split allowed:
    In this case the path is from the left sub tree, through the node, through the right sub tree
    E.g: 8->5->9
    2. Split not allowed:
    In this case the path is either from the left sub tree till the node or right sub tree till the node
    E.g: 8->5 & 9->5
    3. No path:
    Consider a case where:
      8
      |
     / \
    -9 -9
    In such a case it's better not to traverse from 8. The max. path sum is 8 itself
    4. Path through the parent node
    In such a case split is not allowed from the current node, the max. split not allowed sum 
    is passed to the parent node which is then used by the parent node to calculate sums for various cases
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def maxPathFromNode(root):
            if not root:
                return 0
            left_sum = maxPathFromNode(root.left)
            right_sum = maxPathFromNode(root.right)
            sum_with_split = left_sum + right_sum + root.val # Path is from left-sub tree -> curr node -> right-sub-tree
            sum_without_split = max(left_sum, right_sum) + root.val # Path is either from left-sub-> curr node or right-sub->curr node
            #print(f'{root.val}:{left_sum}:{right_sum}')
            nonlocal res
            res = max(res, sum_with_split, sum_without_split, root.val)
            return max(sum_without_split, root.val) 
            # Path used by the parent node can either be the max sum without spit 
            # OR the value of the curr node itself. This is important for cases 
            # where the max sum without split is -ve while the curr. node val. is +ve
        maxPathFromNode(root)
        return res