"""
417. Pacific Atlantic Water Flow
Solved
Medium
Topics
premium lock icon
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

class Solution:
    """
    Brute Force BFS Approach
    Logic:
    Visualize this as a directed graph where the current cell is the start node
    This node can be connected to (curr->other) other nodes horizontally or vertically
    but only if the values of those nodes are less that the curr node's values

    We run BFS from each node & visit all neighbors & keep track of whether it has
    neighbors adjacent to both the atlantic or pacific ocean
    If yes then we add it to the result list

    Return the result list

    Time Complexity = O(m.n)^2
    Because we do it for every single cell of the grid - m.n
    & we run BFS for every single cell, in worst case this can be - m.n
    Total TC. = O((m.n).(m.n)) = O(m.n)^2

    Minor Optimization:
    We can keep a hashset of nodes that can reach both pacific & atlantic ocean
    If this node is encountered during traversal, it means a path to both exists
    & we can stop traversing for that node immediately.
    But still, in the worst case T.C holds
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []

        def bfs(r, c):
            po, ao = False, False
            hashset = set()
            q = collections.deque()
            q.append([r, c])
            hashset.add((r, c))
            while q:
                x, y = q.popleft()
                if x == 0 or y==0:
                    po = True
                #nonlocal rows, cols
                if x == rows-1 or y==cols-1:
                    ao = True
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dx, dy in directions:
                    if x+dx in range(rows) and y+dy in range(cols) and (x+dx, y+dy) not in hashset:
                        if heights[x+dx][y+dy] <= heights[x][y]:
                            q.append([x+dx, y+dy])
                            hashset.add((x+dx, y+dy))
            return ao and po

        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    res.append([i, j])

        return res