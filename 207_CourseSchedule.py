"""
207. Course Schedule
Solved
Medium
Topics
premium lock icon
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

class Solution:
    """
    Depth First Search

    WHAT WENT WRONG?
    In my initial approach in these problems I tried implementing both DFS & BFS
    With the assumption that if the node was already visited it must be flagged as a cycle
    This was wrong. In DFS or BFS A NODE ALREADY VISITED DOES NOT INDICATE A CYCLE
    e.g.: 1->3---->5
             |     ^
             V     |
             4-----|
        There is no cycle in this directed graph however 5 can be reached from both 3 & 4
        At some pt 5 will be visited but encountering it again 
        DOES NOT MEAN THE GRAPH IS CYCLIC

    But then how do we determine if a cycle exists in a graph?
    1. Kahn's Algorithm - Use this algorithm to determine if a cycle exits
    2. Use another datastructure in DFS/BFS 

    Method 2 - Using a hashset to detect cycles in directed graphs using DFS/BFS
    Let's consider DFS for this approach
    In DFS we go as deep as possible down a path, then explore the next path at each node
    We use the visited set to ensure we don't keep going down the same paths
    not to check if there is a cycle or not
    But when we are going down a path & keep track of all the nodes encountered in the current path
    and meet a node that we already encountered in the same path it means we have a cycle
    E.g: 1->2->1 Current path = [1, 2] then when we encounter 1 again it means this is a cycle

    Algorithm:
    1. We simulate the graph using an adjacency map:
    each node is mapped to all the incoming connections

    2. We use visited set -> Keep track of all the nodes encountered during the entire DFS
    This would help us prevent going down the same paths 
    It would also help us save time, more on that later
    visiting set -> Keep track of all the nodes encountered in the current path
    this ensures there are no cycles present

    3. How dfs function works:
        1. If the node is in visiting - We encountered this node in the same path
            cycle exits return False
        2. If the node is in visited - The rest of the path has been traversed previously
        We can exit with True since it a cycle had existed, the logic would have flagged it
        & returned it to the user early on. This saves time

        3. Else add the node in visiting - to keep track of all nodes along the current path
        4. For all neighbors of the current node, perform dfs
        If dfs returns False, break & return false
        5. If dfs is True, then it means that all the paths from this node do not end in cycles
        6. Remove node from visiting since we are going to explore a new path in the next call
        7. Add the node to visited to ensure we don't waste time traversing this node again
        8. Return True

    4. To ensure no cycles exist in the entire graph, run dfs from every node of the graph

    Time complexity = O(n+e) n->nodes e->edges
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}
        #hashmap = defaultdict(set)
        for c, p in prerequisites:
            hashmap[c].append(p)

        visited = set()
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for p in hashmap[course]:
                if not dfs(p): return False

            visiting.remove(course)
            visited.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True