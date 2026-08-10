"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

class Solution:
    """
    Stack approach
    Element of stack -> [temp, index] where index corresponds to the temp's index in the list
    Iterate over the loop:
        When a temp greater than stack's top element temp is encountered
            This means the current index (current day's) temp is greater than the top element of the stack i.e, a hotter day
            So the result[top element's day] = current day - top element's day
            Pop the top element
        Once the temp is no longer greater it means stack is either empty or a hotter day is the top element
        We still need to find a hotter day for the current day
        So push it to the top of the stack
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stack_temp, index = stack.pop()
                res[index] = i - index
            stack.append([t, i])
        return res