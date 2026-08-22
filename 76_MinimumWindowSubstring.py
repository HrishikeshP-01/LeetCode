"""
76. Minimum Window Substring
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution:
    """
    Sliding Window + Hashmap approach
    Algorithm:
    We are just concerned with the char count of t matching with 
    corresponding char count of the window
    We increase j i.e, slide the window to right:
        with every single iteration
    We decrease i i.e., slide the window / decrease window size when a smaller soln can be obtained. This happens when:
        The char at i is not present in t which means it's not needed
        If hash_s[s[i]] > hash_t[s[i]] this means more than enough characters exist in the window we can decrease the size without affecting the result
    If a match is obtained we update result depending on the length

    1. Why use a dict here?
    We don't need to store all the character counts just the ones we need in this case, just the characters in t
    We need to factor in duplicates as well hence a dict is used to store count
    As per the constraints the char ranges from A-Z & a-z so arrays could be difficult to deal with
    
    Why use a result_found flag?
    We set the result to s by default.
    But there's an edge case:
    s = 'AAA'
    t = 'BBB'
    there's no possible solution
    So when a match is found we use the flag to indicate a possible solution exists
    If no soln. exists we need to return an empty string
    """
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        hash_s = {}
        hash_t = {}
        for c in t:
            hash_t[c] = 1 + hash_t.get(c, 0)
        
        i, j = 0, 0
        matches = 0
        result = s
        result_found = False
        while j<len(s):
            hash_s[s[j]] = 1 + hash_s.get(s[j], 0)
            if s[j] in t and hash_t[s[j]] == hash_s[s[j]]:
                matches += hash_t[s[j]]
            while i<=j:
                if s[i] not in t:
                    i+=1
                elif s[i] in t and hash_s[s[i]] > hash_t[s[i]]:
                    hash_s[s[i]] -= 1
                    i += 1
                else:
                    break
            if matches == len(t):
                result_found = True
                result = s[i:j+1] if len(s[i:j+1]) < len(result) else result
            j+=1
        if result_found:
            return result
        return ''

        
