"""
695. Max Area of Island
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

class Solution:
    """
    BFS Approach
    Very similar to Problem 200 - Number of Islands
    Here we just need to keep track of the area which is basically
    the count of the connected nodes
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        hashset = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = collections.deque()
            curr_area = 1
            q.append([r, c])

            while q:
                x, y = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dx, dy in directions:
                    if x+dx in range(rows) and y+dy in range(cols) and grid[x+dx][y+dy]==1 and (x+dx, y+dy) not in hashset:
                        curr_area += 1
                        hashset.add((x+dx, y+dy))
                        q.append([x+dx, y+dy])
            return curr_area
             
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in hashset:
                    hashset.add((r, c))
                    curr_area = bfs(r, c)
                    #print(curr_area)
                    max_area = max(max_area, curr_area)
        return max_area
        