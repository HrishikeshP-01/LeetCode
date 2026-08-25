"""
23. Merge k Sorted Lists
Solved
Hard
Topics
premium lock icon
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Divide & Conquer +  MERGE SORT
    OPTIMAL APPROACH
    Time Complexity = O(nlogk)

    Logic:
    For every 2 lists in the array perform a merge sort
    The new array of lists is sorted results from the previous step
    Do this till only 1 array is left, that's the result

    Why is the TC O(nlogk)?
    Say we have k lists 
    In the previous sub-optimal approach what we were doing was essentially:
    5 3 7 8
    | | | |
      3
    |   | |
    5   | |
        7 |
          8
    n = 1 here, k=4 we did n.k = 1.4 = 4 steps
    Here, what we are doing is:
    5 3 ,7 8
    | 3 ,7 |
    5   ,  8
      3 ,|
    5   ,|
        ,7 8
    We still have to go through all n elements, but we only have to do it logk times
    Think of it this way:
    TC of merge sort is n
    We are doing merge sort log(k) times
    TC = nlogk
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1: # Edge case. If the list is empty we can't access list[0]
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merged_result = self.mergeLists(l1, l2)
                merged_lists.append(merged_result)
            lists = merged_lists
        return lists[0]
        
    def mergeLists(self, list1: ListNode, list2: ListNode)->ListNode:
        dummy = ListNode(0)
        head, curr = dummy, dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return head.next
            

            
        