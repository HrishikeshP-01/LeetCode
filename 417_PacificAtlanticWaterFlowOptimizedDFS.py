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
    Optimized DFS Approach
    Obtained by REVERSE THINKING

    They have asked us to find all the cells that can reach both the pacific & atlantic ocean
    Obvious approach is to go to each cell & try to find if both oceans are reachable that gives
    you O(m.n)^2 Time Complexity

    But using reverse thinking:
    Certain cells are reachable from the pacific
    Certain cells are reachable from the atlantic
    What we need is the intersection of these 2 sets

    Instead of trying to find if each individual cell can reach an ocean
    We start from the shoreline of that ocean & do a dfs & store all the cells from 
    which water can reach the shoreline.
    We use 2 sets - for the pacific & atlantic each

    The result are the cells that are present in both the pacific & atlantic sets

    Time Complexity:
    Instead of doing dfs for all m.n cells
    We can now do dfs for just shoreline cells
    But each cell is explored only once for both sets
    DFS cost for pacific = O(mn)
    DFS cost for atlantic = O(mn)
    Total TC = O(mn)+O(mn) = O(mn)
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        hashset_pacific = set()
        hashset_atlantic = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, hashset):
            if (r, c) not in hashset:
                hashset.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                if r+dx in range(rows) and c+dy in range(cols) and (r+dx, c+dy) not in hashset and heights[r+dx][c+dy]>=heights[r][c]:
                    dfs(r+dx, c+dy, hashset)
        
        # Find Graph Pacific
        for x in range(cols):
            dfs(0, x, hashset_pacific)
            dfs(rows-1, x, hashset_atlantic)
        for i in range(rows):
            dfs(i, 0, hashset_pacific)
            dfs(i, cols-1, hashset_atlantic)

        result = []
        for i in hashset_pacific:
            if i in hashset_atlantic:
                result.append([i[0], i[1]])
        return result
       