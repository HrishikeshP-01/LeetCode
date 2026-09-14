"""
295. Find Median from Data Stream
Solved
Hard
Topics
premium lock icon
Companies
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

class MedianFinder:
    """
    IMPORTANT: THE FOLLOW UP OPTIMIZATIONS HAVE NOT BEEN ADDRESSED HERE
    COME BACK TO THIS LATER

    Min & Max Heap Approach
    Logic:
    Let stream at any given pt be = [1 2 3 4 5 6 7]
    This can be divided into:
        small -> [1 2 3]
        large -> [4 5 6 7]
        median = large[0]
    Else let stream at next addition be = [1 2 3 4 5 6 7 8]
    This would be divided into:
        small -> [1 2 3 4]
        large -> [5 6 7 8]
        median = (small[-1]+large[0])/2

    Patterns here:
    1. We need the max. value of numbers in small
    2. We need the min. value of numbers in large
    3. Most importantly:
        The size of large & small can either be equal: len(large) = len(small) 
        or large can be 1 number more than small: len(large) = len(small) + 1
        
    We need a way to maintain large & small so that median can be calculated at any time
    To get the max. value of small in O(1) & min. value of large in O(1)
    While keeping insertions & deletions optimized O(log(n))
    We can use a max. heap for small & min. heap for large

    Algorithm:
    1. If small is valid & the number to be inserted is less than max. value in small,
    the number belongs to small, push it into small
    2. Else push the number into large since this could mean small is empty as of now
    OR the number is greater than small's max. value
    3. If the len(small) > len(large) this can't be allowed so pop the largest val. from small
    push it into large
    4. If the len(large) > len(small)+1 this can't be allowed as it no longer has the median 
    as the 1st element so pop from large & push into small

    5. Now, if the len(large)+len(small) is odd, the median is the smallest value in large
    Else if it's even, the median = (small[0]+large[0])/2 
    """
    def __init__(self):
        self.smallHeap = [] # This is a MaxHeap
        self.largeHeap = [] # This is a MinHeap
        heapq.heapify(self.smallHeap)
        heapq.heapify(self.largeHeap)

    def addNum(self, num: int) -> None:
        if self.smallHeap and num < -self.smallHeap[0]:
            heapq.heappush(self.smallHeap, -num)
        else:
            heapq.heappush(self.largeHeap, num)
        if len(self.smallHeap) > len(self.largeHeap):
            x = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -x)
        if len(self.largeHeap) > len(self.smallHeap)+1:
            x = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -x)

    def findMedian(self) -> float:
        left, right=0,0
        #print(self.smallHeap)
        #print(self.largeHeap)
        if self.smallHeap:
            left = -self.smallHeap[0]
        if self.largeHeap:
            right = self.largeHeap[0]
        if (len(self.smallHeap) + len(self.largeHeap)) % 2 == 0:
            return (left+right)/2
        return right


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()