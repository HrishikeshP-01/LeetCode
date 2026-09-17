"""
Number of Connected Components in an Undirected Graph
Medium
Topics
Company Tags
Hints
You have an undirected graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.


Example 1:



Input:
n = 5, edges = [[0,1],[1,2],[3,4]]

Output: 2

Example 2:



Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ < n
0 <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Implement Weighted Union Find
        arr = [-1]*n # Nodes are from 0-n-1 so this is enough

        """
        This is normal find with greater Time Complexity
        def find(n):
            if arr[n]>-1:
                return find(arr[n])
            return n
        """
        # Find with Path Compression for less time complexity
        def find(n):
            if arr[n]<0:
                return n
            arr[n] = find(arr[n]) # This flattens the tree
            return arr[n]

        def union(n1, n2):
            parent_n1 = find(n1)
            parent_n2 = find(n2)
            if parent_n1 == parent_n2:
                return # There could be cyclic edges
                # but we can just skip over them since the graph is connected
                # & that is what we are here to find
            if abs(arr[parent_n1])>abs(arr[parent_n2]):
                arr[parent_n1]+=arr[parent_n2]
                arr[parent_n2]=parent_n1
            else:
                arr[parent_n2]+=arr[parent_n1]
                arr[parent_n1]=parent_n2
        
        # Run the set creation operation
        for x, y in edges:
            union(x, y)

        # Traverse the array & find the number of parents
        count = 0
        for i in arr:
            if i<0:
                count += 1
        return count