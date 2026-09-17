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
    DFS Approach

    For each land encountered, check if it exists in the hashset. If not it's part of a new
    unencountered island.
    Increment the island count. Add it to the connected_islands list
    Now do DFS 
    While connected_islands list is valid 
    Pop out a value -> curr
    Add curr to the hashset
    for each land encountered which is adjacent to curr
    Add it to the connected_islands list
    This way all the land connected to the newly encountered island gets added to the hashset
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        hashset = set()
        connected_islands = []
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j]
                if curr=='1' and (i, j) not in hashset:
                    island_count += 1
                    connected_islands = [(i, j)]
                while connected_islands:
                    x, y = connected_islands.pop()
                    if (x, y) in hashset:
                        continue
                    hashset.add((x, y))
                    if x+1 < len(grid) and grid[x+1][y]=='1':
                        connected_islands.append((x+1, y))
                    if x-1 >= 0 and grid[x-1][y]=='1':
                        connected_islands.append((x-1, y))
                    if y+1 < len(grid[x]) and grid[x][y+1]=='1':
                        connected_islands.append((x, y+1))
                    if y-1>=0 and grid[x][y-1]=='1':
                        connected_islands.append((x, y-1))
        return island_count

