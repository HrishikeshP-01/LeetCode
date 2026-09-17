"""
994. Rotting Oranges
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

class Solution:
    """
    Multsource BFS Approach

    Logic:
    Say we have something like:
       A B C D E
    A  2 1 1 1 2
    B  1 1 1 1 1
    A single BFS at each rotten node would not give us the least time for a fresh orange
    to become rotten: A,E would be rotten at time=1 but how would be know that if we do 
    a single BFS from A,A
    One way is to store the min time to be rotten for each node but that increases complexity
    But if we did multisource BFS approach:
    At Time = 1 the oranges become
       A B C D E
    A  2 2 1 2 2
    B  2 1 1 1 2
    
    But how do we know if there are any fresh oranges left?
    We keep a count of the fresh oranges & for every orange that gets rottent, decrement the count
    If the final fresh count is 0, all oranges have turned rotten


    WHAT WENT WRONG:
    I tried implementing something similar to the code commented below:
    1. I created a second grid to store the min cost of traversal from rotten node to that node
    2. The default cost of traversal = col*row count which is an impossible value
    if the fresh orange was reachable by a rotten orange
    3. Then I'd do dfs from each rotten orange & store the min cost of traversal at each fresh node
    4. If any fresh  orange has the default cost, it's still fresh so return -1
    else return the max. value of the cost
    However, I implemented DFS which traverses the deepest nodes first. So if I had something like:
    2 1
    1 1 
    DFS would do
    2 1 -> 2 1 -> 2 1 -> 2 2
    1 1    2 1    2 2    2 2
    Max. cost would be 3 instead of 2
    I should have implemented BFS here.
    But even if I had implemented BFS it would be a less optimal solution as 
    I would have to do BFS from each rotten node, calculate the final cost etc.
    Instead a multisource BFS would give the answer in O(m.n)
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: # If orange is fresh, update fresh count
                    fresh+=1
                if grid[i][j] == 2: # If orange is rotten, push it into q for multisource BFS
                    q.append([i, j])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh:
            for i in range(len(q)): 
                # The current entries in the q contains all the current level of rotten oranges to be explored
                # We pop them all out & store the next level to ensure that all oranges that could get rotten at 
                # this particular time interval gets rotten
                x, y = q.popleft()
                for dx, dy in directions:
                    if x+dx in range(rows) and y+dy in range(cols) and grid[x+dx][y+dy]==1:
                        grid[x+dx][y+dy]=2
                        q.append([x+dx, y+dy])
                        fresh -= 1
                        # Why does BFS work without a hashset here?
                        # Because we only insert fresh oranges
                        # Once a fresh orange is encountered, we mark it as rotten, ensuring it
                        # never gets added to the queue again
            time += 1

        return time if not fresh else -1


"""
--------------WRONG APPROACH---------------------------
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        default_cost = rows*cols
        cost_grid = [[default_cost]*cols for i in range(rows)]

        visited = set()
        def dfs(x, y, cost):
            visited.add((x, y))
            cost += 1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                if (x+dx) in range(rows) and (y+dy) in range(cols) and grid[x+dx][y+dy]==1:
                    cost_grid[x+dx][y+dy] = min(cost_grid[x+dx][y+dy], cost)
                    if (x+dx, y+dy) not in visited:
                        dfs(x+dx, y+dy, cost)
            print(cost_grid)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    dfs(i, j, 0)
                    #print(cost_grid)
                    visited = set()

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and cost_grid[i][j] == default_cost:
                    return -1
                if grid[i][j]==1:
                    result = max(result, cost_grid[i][j])
        return result
"""