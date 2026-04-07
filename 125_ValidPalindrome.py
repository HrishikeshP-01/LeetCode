"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
T.C = O(n/2) = O(n)
"""

class Solution:
    """
    2 Pointer approach
    Algorithm:
    i -> pointer at beginning of string
    j -> pointer at end of string
    Convert the whole string to lowercase
    Check until i<j (i==j is the middle element, it has no corresponding element)
    if i or j is not alphanumeric increment or decrement & start the check again
    """
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        s = s.lower()
        while i<j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True