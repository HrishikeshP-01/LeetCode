class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort method
        # If we want to keep the space complexity O(1)
        # We can sort the strings first & then compare them
        return sorted(s) == sorted(t)