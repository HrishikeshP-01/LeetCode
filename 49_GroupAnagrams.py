"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        HashMap method
        Idea:
        Given that each string will only contain characters a-z
        So each string can be represented as an array of 26 elements
        Each element corresponding to the count of each character
        Create a hashmap with such arrays and add the string to the list of values for each such array
        Return the values of the hashmap (these will be lists)
        """
        anagramGroups = defaultdict(list) # Automatically creates an empty list for a key, the first time it's accessed making it safer, cleaner
        for s in strs:
            counter = [0] * 26 # Create an array of 26 0s
            for c in s:
                counter[ord(c) - ord('a')] +=1
            
            anagramGroups[tuple(counter)].append(s) # Lists are mutable & can't be dict keys, Tuples are immutable & hashable so they can be used instead

        return list(anagramGroups.values())