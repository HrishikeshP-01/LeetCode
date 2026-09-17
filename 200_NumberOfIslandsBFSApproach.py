"""
200. Number of Islands
Solved
Medium
Topics
premium lock icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    """
    BFS Approach
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        hashset = set()
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r, c):
            q = collections.deque()
            hashset.add((r, c))
            q.append([r, c])
            while q:
                x, y = q.popleft() # Change this to pop() to make it DFS
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dx, dy in directions:
                    if x+dx in range(rows) and y+dy in range(cols) and grid[x+dx][y+dy]=='1' and (x+dx, y+dy) not in hashset:
                        q.append([x+dx, y+dy])
                        hashset.add((x+dx, y+dy))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in hashset:
                    island_count += 1
                    bfs(r, c)
        return island_count