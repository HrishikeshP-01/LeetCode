"""
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Example 2:

Input: target = 10, position = [3], speed = [3]

Output: 1

Explanation:

There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]

Output: 1

Explanation:

The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106
"""

class Solution:
    """
    Stack Approach

    Since cars can't be overtaken, 
    it means that if the time taken by your car to reach the finish line is less than the car in front
    it meets that car along the way at some point and forms a bucket with it

    Find the time taken by each car to reach the destination
    Now sort cars by position, we could have sorted it in descending order but in the below code I was unaware how to do that
    But made up for that in the for loop by iterating in reverse
    This way the stack will contain the time taken by the cars in descending order of their positions, i.e, the cars closes to the destination
        If the time taken by the current car is less that the time taken by the car if front
        The cars will meet at some point & form a bucket
        So no need to add the current car to the stack

        If the time taken by the car is greater than the top time in the stack
        It means this car will reach only after all the buckets in front of it reaches the destination
        So this is a new bucket & an entry is created in the stack

    The final number of buckets it the length of the stack
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_taken = [0]*len(position)
        for i in range(len(position)):
            time_taken[i] = (target-position[i])/speed[i]
        sorted_pos, sorted_time = zip(*sorted(zip(position, time_taken)))
        buckets = []
        #print(sorted_pos)
        #print(sorted_time)
        for i in reversed(range(len(sorted_time))):
            if buckets and buckets[-1]>=sorted_time[i]:
                continue
            buckets.append(sorted_time[i])
        return len(buckets)

