class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hashmap method

        # Check if lenghts are equal
        if len(s) != len(t):
            return False
        
        """
        Create hashmaps of s & t, store the count of occurence of each character
        Then compare the counts and if they're not equal, they aren't a hashmap
        """
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # Using get here bc if s[i] doesn't exist it won't throw an error & will return 0 instead
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countT:
            if countT[c] != countS.get(c, 0):
                return False

        return True

# Time complexity - O(S + T)
# Space complexity - O(S + T)