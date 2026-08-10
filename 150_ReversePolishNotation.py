"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

class Solution:
    """
    Stack Approach
    Push every number into the stack
    When an operator is encountered, pop the last 2 numbers
    Perform the operation & then push the result back into the stack
    Since the problem guarantees valid inputs this approach doesn't require error handling
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in '+-/*': # isnumeric() fn returns false for -ve numbers so we use this instead
                # the problem guarantees the inputs are valid
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t=='+':
                    stack.append(x+y)
                elif t=='-':
                    stack.append(x-y)
                elif t=='*':
                    stack.append(x*y)
                elif t=='/':
                    stack.append(int(x/y)) # can't use math.floor or x//y (flooring operator) because 6/-100 => -0.06 => -1 (lowest integer) 
                    # We want it to truncate toward 0
                    # int() conversions just strip the decimal portion so 0.11 & -0.11 give 0 
            #print(stack) # Print statements in final soln. increase run time
        return stack[0]
        