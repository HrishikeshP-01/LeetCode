class Solution:
    """
    The 2-pointer approach is an optimal solution
    This is a very basic approach that takes more time
    Algorithm:
    forward -> the alphanumeric, lowercase elements of the string in original order
    reverse -> the alphanumeric lowercase elements of the string in reverse order
    Iterate through all elements of the array
    Add the element to the end of forward & to the beginning of reverse
    Compare forward & reverse, return True if same
    T.C = O(n) + O(n)
    """
    def isPalindrome(self, s: str) -> bool:
        forward, reverse = '', ''
        s = s.lower()
        for c in s:
            if not c.isalnum():
                continue
            forward = forward + c
            reverse = c + reverse
        return forward == reverse