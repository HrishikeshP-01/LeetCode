"""
133. Clone Graph
Solved
Medium
Topics
premium lock icon
Companies
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

ONE NUANCE I MISSED HERE:
For a graph 1<->2
This is an undirected graph so neighbors of 1 = [2] & neighbors of 2 = [1]
This didn't impact the solution but this is important to understand

Did I need the hashset?
Couldn't I just use the hashmap to check if I already encountered that node before?

Time complexity = O(E+V) E->Edges, V->Vertices
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    """
    DFS Approach
    Logic:
    We need to store the copy equivalent of each node in order to assign neighbors 
    as needed - for this we'll use a hashmap
    Since this is a cyclic graph should traverse a node only once
    We can use the same hashmap for keeping track of the nodes traversed

    1. Implement a recursive funciton dfs & pass the start node
    2. If a node has not been encountered, it means the copy doesn't exist
    Create a new copy & map it to the node
    3. Now populate the neighbors:
        1. If the neighbor has not been encountered before it means the copy doesn't exist
        the neighbor node hasn't been explored in depth i.e, do dfs here
        2. Once it returns, the node & connected nodes to it has been explored, copies made
        we can add the copy to the list of neighbors

    Return the copy equivalent of the start node
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        if not node:
            return None

        def dfs(node):
            if node not in hashmap:
                hashmap[node] = Node(node.val)
            for n in node.neighbors:
                if n not in hashmap:
                    dfs(n)
                hashmap[node].neighbors.append(hashmap[n])

        dfs(node)
        return hashmap[node]
