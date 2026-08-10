"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    """
    Stack + Hashmap approach
    Hashmap used for fast lookups & avoiding if statements
    """
    def isValid(self, s: str) -> bool:
        hash = {'{':'}', '(':')', '[':']'}
        stack = []
        for i in s:
            if i in '{[(':
                stack.append(i)
            # Check if Stack is empty to capture use cases like ')', '()]' etc. and then check against the hashmap
            elif stack and hash[stack[-1]]==i:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        return False

        