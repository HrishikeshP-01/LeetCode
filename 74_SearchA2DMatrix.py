"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

"""
Both approaches uses Binary Search
Solution 1 is marginally better because here:
Worst Case Scenario = O(log(m)+log(n)) = O(log(m*n))
Best Case Scenario = O(log(m))  - When the number isn't in any of the rows
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, u = 0, len(matrix)-1
        row_number = -1
        while l<=u:
            mid = int((l+u)/2)
            if matrix[mid][0] > target:
                u = mid - 1
            elif matrix[mid][len(matrix[0])-1] < target:
                l = mid + 1
            else:
                row_number = mid
                break
        if row_number == -1:
            return False
        l, u = 0, len(matrix[0])-1
        while l<=u:
            mid = int((l+u)/2)
            if matrix[row_number][mid] < target:
                l = mid + 1
            elif matrix[row_number][mid] > target:
                u = mid - 1
            else:
                return True
        return False
        
"""
Time complexity is the same in all cases = O(log(m)*log(n))
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, u = 0, len(matrix)-1
        row_number = -1
        while l<=u:
            mid = int((l+u)/2)
            if matrix[mid][0] > target:
                u = mid - 1
            elif matrix[mid][len(matrix[0])-1] < target:
                l = mid + 1
            else:
                row_number = mid
                l, u = 0, len(matrix[0])-1
                while l<=u:
                    mid = int((l+u)/2)
                    if matrix[row_number][mid] < target:
                        l = mid + 1
                    elif matrix[row_number][mid] > target:
                        u = mid - 1
                    else:
                        return True
                return False
        return False        