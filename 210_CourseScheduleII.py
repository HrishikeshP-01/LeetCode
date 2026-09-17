"""
210. Course Schedule II
Solved
Medium
Topics
premium lock icon
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

class Solution:
    """
    DFS Search 
    Very similar to the Course Schedule Problem

    Let result =[] be the list of courses in order to be completed
    Keep track of visiting & visited sets to detect a cycle

    DFS logic
    For each node:
    1. If the node is in visitng set it means it was already encountered along this path
    this is a cycle return False
    2. If the node is present in visited, the rest of the paths from this node have
    already been explored, this is confirmed not be a cycle
    Also these nodes have already been completed (they have been added to the result list)
    3. Add the node to visiting
    4. For every neighbor of the node perform dfs
    5. Remove the node from visiting
    6. Add it to visited
    7. Add the node to result.
    Why add the node to result here? Why did we add it only after the neighbors were added?
    Because in the hashmap we created:
    0 : [1, 2, 3]
    This means the course 0 has prerequisites 1, 2, 3
    To complete it we need to complete 1, 2, 3
    So in the logic, the neighbors 1, 2, 3 are eventually added to results
    Only then does 0 get added to result

    Run DFS for each course 
    If a cycle is detected at any course, we can never finish all courses return False
    Else return result

    Time Complexity = O(n+e)
    """
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        hashmap = {i:[] for i in range(numCourses)}
        for n, p in prerequisites:
            hashmap[n].append(p)

        visited = set()
        visiting = set()
        result = []

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for x in hashmap[i]:
                if not dfs(x): return False
            visiting.remove(i)
            result.append(i)
            visited.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return result


