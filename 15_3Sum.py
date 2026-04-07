"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    """
    2 Pointer Approach 
    Once we sort the array, we can fix a number 
    & then use a 2-Pointer approach on the remaining elements
    e.g: [-3, 0, 1, 2, 3]
    i -> -3
    Start at l -> 0 r -> 3 Using 2 pointer approach we arrive at
    l -> 1 r -> 2

    But they have specified the sequences need to be unique
    e.g: [-3, -3, 0, 1, 2, 3]
    Must only give [-3, 1, 2] once
    How do we ensure they're only returned once?
    We ensure the value of i doesn't repeat itself
    For each new i we compare against the previous value:
    If it is the same, it has already been considered so increment i

    Finding j & k is standard 2-Pointer Approach

    There is another edge case:
    [-3, 0, 1, 1, 2, 2]
    i -> -3, j -> 1 (j = 2nd element), k -> 2 (k=5th element)
    If we simply update j & k we get the same result
    as 1 & 2 values are present at the 3rd & 4th elements
    Same as before we keep updating j until it's value is different from the current value
    Don't we need to update k as well?
    No because if we update j to a new value,
    the value of k won't satisfy the zero sum condition anyways
    We just need to ensure j gets updated, the std. algorithm will update k as required
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: # Update i till a new value is obtained
                i += 1
                continue
            j, k = i+1, len(nums)-1
            while j<k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else: # three_sum == 0
                    result.append([nums[i], nums[j], nums[k]])

                    # We have to update j beforehand bc nums[j] == nums[j-1] won't always hold true & j needs to be updated if the program has to run forward else it will be stuck in a loop
                    j += 1
                    while j<k and nums[j] == nums[j-1]: # Update j till a new value is obtained
                        j += 1
                
        return result
            