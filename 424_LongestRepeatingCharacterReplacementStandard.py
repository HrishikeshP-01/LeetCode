"""
424. Longest Repeating Character Replacement
Solved
Medium
Topics
premium lock icon
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

class Solution:
    """
    Sliding Window + Hashmap Approach
    Time Complexity = O(26.n) = O(n)
    For each window the character replacement needed is
    The difference between the length of the window & the most frequent character's count
    So we use a hashmap to store the count of characters in the window
    For each iteration:
    1. We update the character count in the hashmap
    2. Find the most frequent character's count
    3. Find the difference between the lenght of the window & the most freq char's count
    4. If it's less than or equal to k, this is a possible sequence:
        a. If it's length is greater than the result so far, update result
        b. Increase window size by updating j to right
    5. If it's greater than k, then the character replacements has exceeded k
        a. Decrease the window size by shifting i by 1
        b. Update the hashmap to reflect the leaving character
    """
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = [0]*26
        i,j = 0,0
        result = 0
        while j<len(s):
            hashmap[ord(s[j])-65]+=1
            most_freq_char_count = max(hashmap)
            differences = (j-i+1)-most_freq_char_count
            if differences<=k:
                result = max(result, j-i+1)
                j+=1
            else:
                hashmap[ord(s[i])-65]-=1
                i+=1
                hashmap[ord(s[j])-65]-=1 
                # This is done because character at j is being updated at the start of the loop
                # Irrespective of whether the differences is > k
                # Without this, when this condition is hit, the same char's count would get incremented twice
        return result
