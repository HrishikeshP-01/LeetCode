# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Logic:
    Preorder = [3, 9, 20, 15, 7]
    Inorder = [9, 3, 15, 20, 7]

    The 1st element of the preorder arr is the root -> 3
    Now to determine which elements belong to the left-subtree & right-subtree of 3:
    Find the index of 3 in the inorder list - 2nd pos (let's call this mid)
    All elements to the left of the 2nd pos in the inorder list belongs to the left sub-tree -> [0]
    All elements to the right of the 2nd pos in the inorder list belongs to the right sub-tree -> [15, 20, 7]

    We can do this iteratively for the left & right sides but for that we need the new preorder lists for the left & right
    The preorder list for the left subtree will contain elements = number of nodes in the left subtree
    We already know the number of nodes: len(inorder[0:mid-1]) = mid = left_size
    The first element of preorder list is the current root, we should pass mid number of nodes AFTER the 1st element
    so left preorder list becomes: [1:mid+1] 
    The right preorder list is the rest of the original preorder array: [mid+1:]
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        left_size = mid+1
        root.left = self.buildTree(preorder[1:left_size], inorder[0:mid])
        root.right = self.buildTree(preorder[left_size:], inorder[mid+1:])
        return root