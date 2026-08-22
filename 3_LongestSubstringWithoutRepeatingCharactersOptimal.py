"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    """
    Sliding Window Approach - Optimal Solution
    1. If the current element at j is present in the set:
        Keep Removing the element at start - the ith position 
        until the element at j is no longer present in the set
    2. Add the element at j to the set
    4. Calcualte the max_len of the substring

    Why this works:
    HRABCACD
    When j -> 6rd element (A) 
    This resulting substring becomes HRABCA which has duplicates
    So we have to update i while removing the ith elements from the set
    until the set doesn't have A
    The resulting substring becomes BCA which is the new substring without duplicates
    This algorithm lets us find all longest substrings without duplicates
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        i, j = 0, 0
        max_len = 0
        while j<len(s):
            while s[j] in store:
                store.remove(s[i])
                i+=1
            store.add(s[j])
            max_len = max(max_len, j-i+1)
            j+=1
        return max_len