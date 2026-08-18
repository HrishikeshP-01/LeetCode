"""
875. Koko Eating Bananas
Solved
Medium
Topics
premium lock icon
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

class Solution:
    """
    Approach: Binary Search
    Logic:
    We need to find the minimum number that enables us to consume the pile within h hours
    What could the possibility space of this min_number be?
    The smallest number is 1
    The largest number = the len of the largest pile
    e.g: [2, 7] h=1000 Koko can eat 1 banana per hour & still finish the pile
    So the solution space is not restricted to the piles array
    Its the numbers between [1...len(largest pile)]

    So we can perform a binary search to find the min number:
    1. Sort the array for the search to work
    2. l_val=1 & u_val=piles[-1]
    3. while l_val<=u_val
        a. Calculate mid_val
        b. Find the time taken to eat the whole pile @ mid_val bananas/hr
        c. If the time is > target h then we need a larger mid_val, so l_val=mid_val+1
        b. If the time is < target h, maybe a lesser solution exists towards the right
        But this is NOT Guranteed which is why we have a min_piles variable to keep track of all successful <=h values
        We update the min_piles
        then we try to find if another lesser solution exists by u=mid_val-1
    4. Return min_piles
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, u = 1, piles[-1]
        min_piles = u
        while l<=u:
            mid = int((l+u)/2)
            time_taken = 0
            for p in piles:
                if p<=mid:
                    time_taken+=1
                else:
                    import math
                    time_taken += int(math.ceil(p/mid))
            #print(f'{mid}:{time_taken}:{h}')
            if time_taken > h:
                l = mid+1
            else:
                min_piles = min(mid, min_piles)
                u = mid-1
        return min_piles