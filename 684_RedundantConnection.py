"""
684. Redundant Connection
Solved
Medium
Topics
premium lock icon
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""


class Solution:
    """
    Cycle detection in an undirected graph
    Union Find Algorithm

    Refer here for detailed explanation: https://youtu.be/wU6udHRIkcc?si=ev1mYyPrKjWXd1BR

    I've used a Weighted Union Approach
    Logic:
    Say there are N nodes from 1-N
    Each index of the array indicates:
        If the index is -ve: Indicates that this node is the parent of its set
        If the index is +ve: Indicates the parent of this node
        If the index is -ve: The value of the index indicates how many nodes are present in the set

    How find works:
    For n:
    if arr[n] < 0 - this is the parent of the set, return n
    if arr[n] >= 0 - we must find the parent find(arr[n]) 
    Collapsing Find
    Note: Find can be made much more faster if we use a Collapsing find approach
    Currently the way we store the parent doesn't optimize the levels in the tree
    eg: 1<-2<-3 this is a possibility, to find parent of 3 we need more than 1 traversals
    However, collapsing find ensures we update the parent of 3 as soon as we find the 
    parent of 2 so the end results looks like:
    1<-2
    ^
    |
    3 Finding the parent takes just 1 traversal i.e., O(1) time 
    Collapsing find, makes the tree more flat which optimizes traversal

    How union works:
    While doing the union of 2 sets, the parent of the tree with more nodes
    will be the new parent, this ensures we lean towards a flat structure for resulting sets
    Using a weighted union approach makes this check easier since the parent indicator
    also stores the weight (number of nodes) of the tree
    Union algorithm
    For 2 nodes x, y
    Find parent of x
    Find parent of y
    if abs(arr[x])>abs(arr[y]) x is the new parent, else y is the new parent
    Update the values of arr[x] or arr[y] to reflect the new number of nodes
    THIS IS IMPORTANT & THE MOST FORGOTTEN STEP
    Then update the parent of the child set to the new parent

    (If it was directed we could have used DFS & visiting, visited sets)
    """
    class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        arr = [-1]*(N+1) # Why N+1 even though there are only N nodes
        # Because Nodes are numbered from 1-N we want arr[x] where x=node val
        # So we use N+1 to have values from 0,1-N

        # How do we know there are N nodes? 
        # It's given that edges make up a tree + 1 cycle edge is guaranteed to be present
        # Meaning All nodes are connected exactly once + 1 cycle edge = N

        def find(n):
            if arr[n] > 0:
                return find(arr[n])
            else: # Base case, arr[n] is -ve this is the parent of the set
                return n

        def union(n1, n2):
            p_n1 = find(n1)
            p_n2 = find(n2)
            if abs(p_n1)>abs(p_n2):
                arr[p_n1] += arr[p_n2] # Update count of nodes in set
                arr[p_n2] = p_n1 # Update parent
            else:
                arr[p_n2] += arr[p_n1] # Update count of nodes in set
                arr[p_n1] = p_n2 # Update parent

        for i, o in edges:
            if find(i) != find(o):
                union(i, o)
            else:
                return [i, o]