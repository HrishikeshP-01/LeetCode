"""
130. Surrounded Regions
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

class Solution:
    """
    Optimized DFS Approach
    Using REVERSE THINKING METHOD

    They have asked us to find all the surrounded regions & mark them as X
    The obvious approach is to check if a node is surrounded if yes, mark it as X
    We could optimize this by using a set of visited nodes but still we have to do the check
    for every node & T.C = O(m.n)^2

    Using reverse thinking: What if we find the unsurrounded regions
    Mark everything else as X
    We start at the edges of the board & do dfs for each O on the edge
    while maintaining a set of visited nodes

    Finally we traverse through all the cells of the board, if it's not in visited
    it's surrounded so mark it as X

    This would take Time Complexity of O(m.n)
    Though we are doing dfs for m+n nodes since we only do it for nodes not in visited
    & since the nodes can traverse horizontally & vertically each node is guaranteed to be visited
    just once
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            if (r, c) not in visited:
                visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                if r+dx in range(rows) and c+dy in range(cols) and board[r+dx][c+dy]=='O' and (r+dx, c+dy) not in visited:
                    dfs(r+dx, c+dy)

        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols-1]=='O':
                dfs(i, cols-1)
        for i in range(cols):
            if board[0][i]=='O':
                dfs(0, i)
            if board[rows-1][i]=='O':
                dfs(rows-1, i)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    board[i][j]='X'
