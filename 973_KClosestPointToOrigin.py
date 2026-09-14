"""
973. K Closest Points to Origin
Solved
Medium
Topics
premium lock icon
Companies
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""

class Solution:
    """
    Min Heap Approach

    Logic:
    Basic logic just know that heapify works by taking the very first value of each entry
    So if elements of an array are arrays like: [[1, 2, 3], [7, 4, 6]]
    The very first value of each element -> 1, 7 are considered during heapify

    With this in mind we just have to store the distance along with the points
    Create a min heap using heapify
    The first k elements of this heap would be the answer

    Time complexity: Heapify of all elements take O(n) time
    Heap pop of k elements takes k.O(log(n)) time
    Total = O(n) + k.O(log(n))

    Alternate solution: A sorting approach could also work here
    It would take O(nlog(n)) time

    Alternate heap solution: Since order doesn't matter try using a maxheap with a fixed k size
    Allow inserts only if the dist is less than the max value
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = x*x + y*y
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        res = []
        i=0
        while minHeap and i<k:
            i+=1
            d, x, y = heapq.heappop(minHeap) # Why do we need heappop every time?
            # Heap doesn't guarantee the rest of the array is ordered
            # It only guarantees that the first element would be the smallest element
            # The second smallest element needs to be found, so we pop to recalculate the smallest element
            res.append([x, y])
        return res
