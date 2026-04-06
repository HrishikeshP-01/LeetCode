"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

class Solution:
    """
    Take example: [100, 1, 200, 4, 3, 101]
    Easiest approach:
    Sort the array
    Find the maximum consecutive sequence length

    But to do it in O(n) time:
    Let's visualize this along the number line: 
    1,2,3,4 ... 100,101 ... 200
    There are 3 buckets
    To get the lenght of a bucket we need to count from the start of the bucket till the end
    How to identify if the number is the start of the bucket?
    The starting number doesn't have any elements preceeding it
    n-1 isn't present in the array => Start of the bucket

    Algorithm:
    We only consider numbers that are the starting numbers of the bucket
    Since counting from makes sense, we don't want to count from the middle of the bucket
    1. Add all elements to a set
    2. Check if a number is the start of the bucket: n-1 in set
    3. If it's not continue for the next number
    4. If it is, start the loop:
    5. Set length to 0
    6. Check if n+length is present in the set
    7. If yes, increment length
    8. Finally when the loop breaks, compare length with the longest sequence length & update the longest accordingly
    9. Once you iterate over all elements of the array, return the longest
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1 # Store the longest sequence length
        num_set = set(nums)

        for n in nums:
            if (n-1) in num_set: # Check if number is the start of the bucket
                continue
            else:
                length = 0
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest