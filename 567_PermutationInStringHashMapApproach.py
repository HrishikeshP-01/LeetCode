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
    Sliding Window + Hash Map Approach
    Time Complexity = O(26.n) = O(n) but it still performs 26 checks each iteration. 
    A solution that takes lesser time exists
    Space Complexity = 2xO(26)

    Approach:
    1. Create hashmaps for s1 & substring of s2
    2. For each window compute the hashmap for the substring of s2
        This is easy since the window slides by 1 element we just have to decrement 
        the count of elmenent leaving the window
        & increment the count of element entering the window
    3. Compare the hashmaps, if they are equal the permutation exists

    Edge cases:
    1. If s1 has more characters than s2, permutation can't exists
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hashmap_s1 = [0]*26
        hashmap_sub = [0]*26
        for i in range(len(s1)):
            hashmap_sub[ord(s2[i])-97]+=1
            hashmap_s1[ord(s1[i])-97]+=1
        i,j = 0, len(s1)-1
        while j+1<len(s2):
            if hashmap_s1 == hashmap_sub:
                return True
            j+=1
            hashmap_sub[ord(s2[j])-97]+=1
            hashmap_sub[ord(s2[i])-97]-=1
            i+=1
        # Edge case, the last substring is calculated but isn't checked
        # Since the loop exits so we do a final check here
        if hashmap_s1 == hashmap_sub:
            return True
        return False

