"""
297. Serialize and Deserialize Binary Tree
Solved
Hard
Topics
premium lock icon
Companies
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    Using the same approach as leetcode
    The serialization is in the form [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right, root.left.left.left, ...]

    Serialization logic:
    Breadth First Search Traversal
    Make sure to handle the case where node is None, You need to insert 'null'
    Also need to add a delimiter. I used ',' 
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        d = deque([root])
        s = ''
        while d:
            for i in range(len(d)):
                n = d.popleft()
                if n:
                    s += str(n.val)+','
                    d.append(n.left)
                    d.append(n.right)
                else:
                    s += 'null'+','
        return s[0:len(s)-1]

    """
    Deserialization logic:
    representation is in the form: root, root.left, root.right, root.left.left, root.left.right ...
    If we have 2 deques:
    Parent -> [root] Child -> [root.left, root.right, root.left.left, root.left.right]
    pop from left of parent & the first 2 nodes in child are the children of this parent
    Next we push these children into the parent deque:
    Parent -> [root.left root.right] Child -> [root.left.left root.left.right root.right.left root.right.right ...]
    The pattern repeats

    Here we have a parent node deque & child val deque, create the child nodes, 
    assign them to parent & push them into parent deque
    Make sure to insert the None nodes as well
    """
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        if arr[0] == 'null': # Edge case - root node is None
            return None
        root = TreeNode(int(arr[0]))
        child_vals = deque(arr[1:])
        parent_nodes = deque([root])
        while parent_nodes:
            p = parent_nodes.popleft()
            l_val = child_vals.popleft()
            r_val = child_vals.popleft()
            if l_val == 'null':
                l = None
            else:
                l = TreeNode(l_val)
                parent_nodes.append(l)
            if r_val == 'null':
                r = None
            else:
                r = TreeNode(r_val)
                parent_nodes.append(r)
            p.left = l
            p.right = r
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))