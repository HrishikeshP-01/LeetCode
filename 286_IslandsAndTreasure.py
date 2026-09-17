"""
Islands and Treasure
Medium
Topics
Company Tags
Hints
You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""

class Solution:
    """
    Multisource BFS

    The obvious answer is to do dfs/bfs from each tile & find the shortest distance to a treasure chest
    But using REVERSE THINKING METHOD
    This becomes a problem of how many steps does it take from the treasure chests
    to all traversable land blocks

    We need the shortest distance from a treasure chest to a landblock & since there are multiple
    treasure chests, we can use multisource BFS & for each new level in the queue
    update the distance by 1    
    """
    def islandsAndTreasure(self, grid: List[List[int]])->None:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i, j])

        distance = 1
        directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    # In range is more expensive than standard comparison, use that if you want an optimized solution
                    if (x+dx) in range(rows) and (y+dy) in range(cols) and grid[x+dx][y+dy]==2147483647:
                        # What ensures the traversed blocks are no longer traversed?
                        # The grid[x+dx][y+dy]==2147483647 ensures only land blocks that have not been visited get added to the deque
                        grid[x+dx][y+dy] = distance
                        q.append([x+dx, y+dy])
            distance += 1
