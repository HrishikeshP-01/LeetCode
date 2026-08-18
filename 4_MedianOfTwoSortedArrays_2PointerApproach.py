"""
4. Median of Two Sorted Arrays
Solved
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
class Solution:
    """
    Two Pointer Approach
    Similar to merge sort:
    Since we know the length of both arrays, their sum is the lenght of the combined array
    So we find the position of median from that
    We keep 2 pointers, each one traversing along an array in merge sort fashion 
    where the smaller elements are traversed first
    Median for odd n -> n/2
    Median for even n -> Average of n/2 - 1, n/2
    To get n/2 - 1 th elment of the combined array, we have a prev variable
    That stores the value of the element just before n/2
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        m_pos = int(n/2)+1
        p1, p2, c=0, 0, 0
        curr, prev = 0, 0
        while c!=m_pos:
            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    prev = curr
                    curr = nums1[p1]
                    p1 += 1
                    c += 1
                    
                else:
                    prev = curr
                    curr = nums2[p2]
                    p2 += 1
                    c += 1
                    
            elif p1 < len(nums1):
                prev = curr
                curr = nums1[p1]
                p1 += 1
                c += 1
                
            elif p2 < len(nums2):
                prev = curr
                curr = nums2[p2]
                p2 += 1
                c += 1
                
        if n%2==0:
            return (prev+curr)/2
        else:
            return curr
            
        
