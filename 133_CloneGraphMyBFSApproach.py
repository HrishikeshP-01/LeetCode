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

from typing import Optional
class Solution:
    """
    Logic: 
    We are essentially traversing the graph, visiting all the nodes once
    For each new node encountered we create a Node() copy if it doesn't already exist
    Then we add neighbors to the this node - we create copies of neighbors if they don't 
    exist at that pt. or we use existing copies

    For this we need:
    Deque - That keeps tracks of all the remaining nodes to be explored
    Hashset - That keeps tracks of all the nodes that have been explored
    Hashmap - That maps the original node to the copy 

    1. Initialization:
        Add the root node to the hashset
        Append the root node to the deque
        Enter the root node & copy equivalent into the hashmap
    2. While the deque is not empty:
        1. Pop the leftmost node - the node to be explored
        2. Get the copy equivalent of the node from the hashmap
        3. For all neighbors of the original node:
            1. If the copy equivalent does not exist:
                Create a copy equivalent & add the entry into the hashmap
                Else get the copy equivalent from the hashmap
                Add the copy equivalent to the list of neighbors
            2. If the neighbor is not present in the hashset, it needs to be explored
                Add it to the deque
                Add it to the hashset - it no longer should be added to the deque again
    3. Return the copy equivalent of the root node
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # Edge case
            return None
        hashset = set()
        hashmap = {}
        q = collections.deque()
        q.append(node)
        hashset.add(node)
        hashmap[node] = Node(node.val)
        while q:
            n = q.popleft()
            n_copy = hashmap[n]
            for neighbor in n.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor] = Node(neighbor.val)
                if neighbor not in hashset:
                    hashset.add(neighbor)
                    q.append(neighbor)
                n_copy.neighbors.append(hashmap[neighbor])
        return hashmap[node]

        
