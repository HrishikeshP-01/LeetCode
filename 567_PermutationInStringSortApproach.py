"""
567. Permutation in String
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    """
    Sliding Window + Sort Approach
    SUBOPTIMAL SOLUTION
    Time Complexity = O(n.mlogm)
    We check for n iteration & for each iteration we sort & compare
    Easy implementation:
    1. Sort s1
    2. For each window sort the substring
    3. Compare sorted s1 & sorted substring. If they are equal, it's a valid permutation
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_start, s_end = 0, len(s1)
        sorted_s1_chars = sorted(s1)
        s1 = ''.join(sorted_s1_chars)
        perm_found = True
        while s_end <= len(s2):
            sub_str = s2[s_start:s_end]
            sorted_sub_str_chars = sorted(sub_str)
            sub_str = ''.join(sorted_sub_str_chars)
            if sub_str != s1:
                s_start += 1
                s_end += 1
                continue
            return True
        return False