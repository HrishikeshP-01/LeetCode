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
    Brute force BFS
    For each O cell find all the connected O cells
    Maintain a flag whether it's surrounded or not
    If an O cell is on the border of the board it's not surrounded

    If the cells are surrounded, use the set to access all the connected O nodes
    & mark these nodes as X

    Time complexity - You are doing this for each node in the cell
    O(m.n)^2

    We could optimie this furhter by using a hashset to store all visited nodes
    in which case number of DFS operations would reduce drastically
    Best case Time Complexity = 1.O(m.n) + O(m.n) = O(m.n) (Where all nodes are Os)
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def bfs(r, c):
            hashset = set()
            q = collections.deque()
            q.append([r, c])
            hashset.add((r, c))
            is_surrounded = True
            while q:
                x, y = q.popleft()
                if x == 0 or x == rows-1:
                    is_surrounded = False
                if y == 0 or y == cols-1:
                    is_surrounded = False
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dx, dy in directions:
                    if x+dx in range(rows) and y+dy in range(cols) and (x+dx, y+dy) not in hashset and board[x+dx][y+dy]=='O':
                        hashset.add((x+dx, y+dy))
                        q.append([x+dx, y+dy])
            if is_surrounded:
                for x, y in hashset:
                    board[x][y] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    bfs(r, c)