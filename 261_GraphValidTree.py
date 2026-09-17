"""
Graph Valid Tree
Medium
Topics
Company Tags
Hints
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.


Example 1:



Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

Output: true

Example 2:



Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

Output: false

Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= a_i, b_i < n
a_i != b_i
There are no self-loops or repeated edges.
"""

class Solution:
    """
    Weighted Union Find Approach
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        arr = [-1]*n

        def find(n):
            if arr[n] > -1:
                return find(arr[n])
            return n

        def union(n1, n2):
            parent_n1 = find(n1)
            parent_n2 = find(n2)
            if parent_n1 == parent_n2:
                return False
            if abs(arr[parent_n1])>abs(arr[parent_n2]):
                arr[parent_n1] += arr[parent_n2]
                arr[parent_n2] = parent_n1
            else:
                arr[parent_n2] += arr[parent_n1]
                arr[parent_n1] = parent_n2
            return True
        # Checks for cycles
        for x, y in edges:
            if not union(x, y): return False

        # Now check for any disjoint nodes
        # Ideally all nodes except 1 must have parent > -1
        """
        count = 0
        for i in range(n):
            if arr[i]<0:
                count+=1
            if count>1:
                return False

        This is the obvious solution but it adds O(n) time complexity
        What is a more O(1) approach?
        Say we have a tree. Every node must be connected to a single parent node
        A tree with n nodes must have exactly n-1 edges
        That's the property of a tree. We can just check if this is satisfied 
        at the beginning
        Also since we are guaranteed by the problem that edges won't be repeated
        or permutations don't exist e.g.: 1,2 & 2,1 won't be present
        this check at the beginning would be enough to eliminate this possibility
        """
        if len(edges)!=n-1: return False

        return True
