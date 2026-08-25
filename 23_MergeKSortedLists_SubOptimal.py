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
class Solution:
    """
    One big Merge Sort

    This is a SUB OPTIMAL APPROACH
    There are k lists & say n is the length of the biggest list
    The steps taken are k.n. In the worst case all lists have n elements. For n iterations I need to make k comparisons
    Time complexity = O(k.n)
    Memory complexity = O(1)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        # Clean up
        while lists: # why use while instead of for loop? Pop operation changes len of list, for loop evaluates len of list only once
            i,j = 0, len(lists)
            while i<j:
                if not lists[i]:
                    lists.pop(i)
                    j-=1
                    i-=1
                i+=1
            if len(lists) == 0:
                return head.next
            min_node = lists[0]
            min_node_pos = 0
            for i in range(len(lists)):
                if lists[i].val < min_node.val:
                    min_node = lists[i]
                    min_node_pos = i
            curr.next = min_node
            curr = curr.next
            lists[min_node_pos]=lists[min_node_pos].next
        return head.next
            

            
        