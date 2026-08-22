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
    Sliding Window + Optimized Hash Map Approach
    Time Complexity = O(26) + O(n) = O(n). 
    A solution that takes lesser time exists
    Space Complexity = 2xO(26)

    Approach:
    1. Create hashmaps for s1 & substring of s2
    2. Instead of comparing hashmaps at each iteration we use a variable -> matches
    matches stores the count of how many matches exist in the hashmap
    For example: s1 = 'aa' s2='bb' Matches=24, they differ at positions 0 & 1 of the hashmap
    If matches = 26 this means each element of the hashmap is equal to the corresponding 
    key in the second hashmap i.e., a perumation exists
    3. To update the hashmap of the substring we use the sliding window approach
        a. When the left index gets shifted by 1 we need to check if the 
        hashmap value of the letter in the old index was equal to the hashmap value of the letter at s1
        If yes we need to decrement match since the left is shifting & that letter is no longer part of the substring
        
        Since we are shifting the index, we decrement the hashmap value & check the updated value
        with the hashmap value of s1. If it's equal then a new element is matching so we
        increment match

        b. Similarly, we update j
        If the hashmap value at the new j already matches with the corresponding s1 hashmap value
        We need to decrement matches since the letter is going to be added & the count will become unequal
        
        Since we are shifting the index of j, we increment the hashmap value & check the updated value
        with the hashmap value of s1. If it's equal then the new element is matching so we increment match

    Edge cases:
    1. If s1 has more characters than s2, permutation can't exists
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case - if s1 has more characters, permutation can't exist
        if len(s1)>len(s2):
            return False

        hashmap_s1 = [0]*26
        hashmap_sub = [0]*26
        for i in range(len(s1)):
            hashmap_s1[ord(s1[i])-97]+=1
            hashmap_sub[ord(s2[i])-97]+=1
        matches=0
        for i in range(26):
            if hashmap_s1[i]==hashmap_sub[i]:
                matches+=1

        i, j=0, len(s1)-1
        while j+1<len(s2):
            #print(s2[i:j+1]+' '+str(matches))
            if matches == 26:
                return True
            if hashmap_sub[ord(s2[i])-97]==hashmap_s1[ord(s2[i])-97]:
                matches-=1
            hashmap_sub[ord(s2[i])-97]-=1
            if hashmap_sub[ord(s2[i])-97]==hashmap_s1[ord(s2[i])-97]:
                matches+=1
            i+=1
            j+=1
            if hashmap_sub[ord(s2[j])-97]==hashmap_s1[ord(s2[j])-97]:
                matches-=1
            hashmap_sub[ord(s2[j])-97]+=1
            if hashmap_sub[ord(s2[j])-97]==hashmap_s1[ord(s2[j])-97]:
               matches+=1

        # Edge case: Since the condition is j+1<len(s2) for the very last substring
        # We don't compare matches so we need to do that here 
        if matches == 26:
            return True
        return False