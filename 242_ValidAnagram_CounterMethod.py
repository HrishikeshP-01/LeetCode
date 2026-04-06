class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hashmap method

        # Manually creating hashmaps to track counts takes more time to execute in python
        # Instead, we can use the Counter data structure that automatically creates a hashmap with a frequency counter for objects provided as input
        # We just need to compare the counters
        # Counters are very useful for huge amounts of data
        if Counter(s) != Counter(t):
            return False
        return True
    

# Time complexity - O(S + T)
# Space complexity - O(S + T)