"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        HashMap approach
        For rows:
        Have a hashmap for each row
        For each element check if it exists in the hashmap corresponding to the row
        If not add the element
        For columns:
        Have a hashmap for each column
        For each element check if it exists in the hashmap corresponding to the column
        If not add the element
        For sub-boxes:
        There are 9 sub-boxes
        How do we identify which element a sub-box belongs to?
        If we number all the sub-boxes based on rows & columns we get:
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2
        We need to map each index from the original matrix
        to each index in this matrix
        We can map r, c => r//3, c//3
        Finally, have a hashmap for each subbox
        If the element isn't present in the corresponding hashmap add it
        """
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.': # if the element is ., that spot is empty
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                # Key of the square hashmap is a tuple 
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
                    