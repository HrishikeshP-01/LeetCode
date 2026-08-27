"""
572. Subtree of Another Tree
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
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
    This is a same tree problem in disguise
    Each node could potentially be the same tree as the Tree B
    If yes then Tree B is a subtree
    So implement a function to check if 2 trees are same
    Iterate throught the original tree & then check if the subtrees are same
    Time Complexity = O(n.m) n-> len of Tree A m->len of Tree B
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, rootA, rootB)->bool:
        if not rootA and not rootB:
            return True
        elif rootA and rootB:
            if rootA.val != rootB.val:
                return False
            return self.isSameTree(rootA.left, rootB.left) and self.isSameTree(rootA.right, rootB.right)
        else:
            return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    NOT A SOLUTION
    !!!!!!!!!!          INCORRECT        !!!!!!!!!!!!!!!!!
    Tried to implement the below in hopes of achieving an O(n) solution 
    But it fails for the following edge cases:
        1        1
        /\
       1  2
    It fails because 1=1 so it moves to the next nodes & compares 1=null? and 2=null?
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif root and subRoot:
            if root.val != subRoot.val:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            else:
                return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        else:
            return False