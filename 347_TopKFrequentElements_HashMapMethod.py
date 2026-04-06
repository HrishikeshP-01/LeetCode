"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Hash + Bucket Sort approach
        Add all the elements into a hashmap while storing the count
        We'll use a variation of bucket sort
        We know that all the possible counts range from 1-n
        Where 1 is when all elements are unique & n is when all elements are same
        We just need to store the element under the particular count
        Then we need to traverse the array backwards & get the top k elements
        """
        # Create a hashmap & store the count
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        result = []
        # Create an array where the indices point to count (max index = n)
        freq = [[] for i in range(len(nums)+1)] # nums + 1 bc we want the last index to be len(nums)
        for key, value in count.items():
            freq[value].append(key)

        # Now iterate through count_array in desc order & get the top k elements
        top_k = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                top_k.append(n)
                if len(top_k)>=k:
                    return top_k