"""
621. Task Scheduler
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""

class Solution:
    """
    Max Heap + Deque Approach

    Logic:
    Let input be [A,B,A,A,B,C,C] & n = 1
    The best approach is to try & complete the task with the highest frequency first
    ABACABC
    else we would have more idle spaces than needed e.g: ABCBCA_A

    Now let's say that a task X was completed at time y
    The next time this task can be used would be when time = y+n

    So:
    1. We'll need to maintain a count of each task
    2. We need a way to get the task with the highest count
    3. We'll need to maintain the time at which each task can be used next

    To achieve 1 -> We can use a Counter
    Counter gives us task:count mapping. However, for the next steps we just need the count
    since each count signifies an individual task we can just use that, no need for keeping track 
    of the task themselves
    So add all the Counter values into an array
    To achieve 2 -> Create a maxHeap from the array, this allows us to get the task 
    with the highest frequency
    To achieve 3 -> We'll use a deque. The leftmost values signifies the task that are
    available at the earliest point in time & the rightmost values signifies the tasks just
    executed & available only after curr time + n

    Algorithm:
    1. While heap or deque has values it means there are tasks pending
    2. Increment time - time is also the result as this represents the CPU intervals needed to complete all tasks
    3. If the heap is valid, pop the max. freq & decrement it:
        this signifies one task has been completed
        Then calculate the time this task can next be used: time + n
        & push both the count & next available time into the deque
    4. If the deque is valid & the leftmost element's available time is equal to the current time
        this means the task is now available to be executed
        Pop it out of the queue and push it into the heap
    5. Once heap & deque are empty it signifies that all tasks are done, return time
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # creates a dict where val = count of each element in tasks
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # Since the cnts are -ve in the max heap adding one decrements it
                if cnt: # Add to queue only if cnt>0 i.e, task is still pending
                    q.append([cnt, time+n]) # time+n is the time this task can be used again
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
