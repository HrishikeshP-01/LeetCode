"""
703. Kth Largest Element in a Stream
Easy
Topics
premium lock icon
Companies
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8
 

Constraints:

0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
"""

class KthLargest:
    """
    Min Heap Approach
    Logic:
    Say we the initial inputs are:
    k = 3, nums = [1, 5, 4, 8]
    We need to keep track of the 3rd largest element
    Elements will only be ADDED to the stream
    So we don't need to bother about elements that are less than the 3rd largest element
    They are never going to be the 3rd largest element since elements before or after are
    NOT GOING TO BE REMOVED
    However if a larger element is going to be added, the 3rd largest element becomes 
    the 4th largest element

    This pattern fits the min heap. 
    If the size of the heap is k then the root node i.e., the first element of the heap
    would be the kth largest element of the entire stream

    Logic while initialization:
    Initialize the heap & add all the elements in the array into the heap
    Then pop elements till the len(heap) == k
    Time complexity of this step = O((n-k).log(n))
    Worst case scenario = O(nlog(n))
    Popping elements from a heap takes O(log(n)) time & this must be done n-k times
    In the worst case k=1 so n-1 ~ n

    Logic while addition:
    If the number is greater than the kth largest element, it could change the value
    So add the number to the heap
    If the size of the heap > k then pop an element
    The new kth largest element is whichever element is at the root node of the heap i.e, the first element

    We could do the above for all cases but I've added a minor optimization:
    If the number to be added is less than the kth largest element then:
    1. If the heap IS AT CAPACITY THEN
    It's never going to be the kth largest element (SINCE REMOVAL OF ELEMENTS ISN'T POSSIBLE)
    So there is no point in adding it to the heap because it'd get popped out immediately
    as the size of the heap would exceed the allowed limit -> k
    2. If the heap IS NOT AT CAPACITY THEN
    It should be added since this could be the new kth largest element
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k: # Edge case: If len(nums) < k this won't happen
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # K is guaranteed to be less than len(nums) so kth values is always valid
        # Minor optimization: If the value to be inserted is less than the kth larges value, inserting it is not going to make a difference
        # We'll only end up popping it
        if len(self.minHeap)==self.k and val < self.minHeap[0]:
            return self.minHeap[0]  
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)