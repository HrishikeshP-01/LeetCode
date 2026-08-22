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
    My Sliding Window implementation - Speed is slow SUBOPTIMAL refer Optimal Solution
    Approach:
    2 pointers mark the beginning & end of windows: w_start & w_end
    We use a set to check if element in the substring has been encountered before or not
    If w_end is present in set, it means the substring already has the character
    So that point is the end of the particular substring with unique characters
    We update the substring if it's the longest substring encountered yet
    Then we empty the set
    Set w_start = w_start + 1 -> This is important because ABAC When we encounter the 3rd A, The next window starts at BAC
    Set w_end = w_start (A new window)
    If w_end character isn't present in the set it means this can be added to the substring
    i.e, the window expands to the right w_end = w_end + 1

    Once we exit the loop there is an edge case: ABCD
    If the string was full of unique characters this means we haven't calculated the length of this
    So we do the longest substring check here too

    Finally return the length

    Few Problems with this approach:
    1. Why reinitialize the set?
    For each iteration, reinitializing the set & capturing elements is unecessary repetition
    This happens because we update w_start by 1 
    Instead we could remove elements from the set until the duplicate element is no longer present in the set
    This logic is explained in detail in the Optimal approach
    2. Why use len(longest_substring)?
    We don't even need to calculate the longest_substr since we only need length 
    & we know the w_start & w_end we can easily find the length
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        w_start, w_end = 0, 0
        store = set()
        longest_substr = ''
        while w_start <= w_end and w_end < len(s):
            if s[w_end] in store:
                if len(s[w_start:w_end]) > len(longest_substr):
                    longest_substr = s[w_start:w_end] 
                store=set()
                w_start = w_start+1
                w_end = w_start
                
            else:
                store.add(s[w_end])
                w_end += 1
        if len(s[w_start:w_end]) > len(longest_substr):
            longest_substr = s[w_start:w_end] 
        return len(longest_substr)
        