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
    Slightly Smarter Sliding Window + Hashmap Approach
    Time Complexity = O(n)
    We don't need to find the maximum of the hashmap each iteration
    Core logic is the same:
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

    HOWEVER:
    Why do we need to find the most_freq_char_count every single time?
    Think of it this way: Our goal is to find the length of max. substring with minimum replacements
    This length is only going to get updated if we find a character count that is GREATER
    THAN OUR CURRENT most frequent character count
    If the current most frequent character count is not as high as the one we had
    then it's not going to be the answer anyways
    So instead of doing iterating over the hashmap every single iteration
    For each new character added, we just check if that character's count is greater than
    the most frequent character count
    If yes we update the most frequent character count
    If not we still go throught the motions, but it's not going to have an impact on our actual answer
    """
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = [0]*26
        i, j = 0, 0
        most_freq_char_count = 0
        result = 0
        while j<len(s):
            hashmap[ord(s[j])-65] += 1
            most_freq_char_count = max(most_freq_char_count, hashmap[ord(s[j])-65])
            differences = len(s[i:j+1]) - most_freq_char_count
            if differences <= k:
                result = max(result, j-i+1)
            else:
                hashmap[ord(s[i])-65] -= 1
                i += 1
            j += 1
        return result
