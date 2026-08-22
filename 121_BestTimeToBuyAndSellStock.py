"""
121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
premium lock icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution:
    """
    Logic:
    The sale can happen only after you have bought a stock
    Your chance of making a profit happens when you buy the stock for the least price possible
    1. Iterate over the array
    2. If the current element is less than min_buy - you can potentially make a higher profit
    3. So BUY, min_buy = current
    4. Else it means that the current value is higher than min_by
    5. Calculate profit generated from potential sale current_profit = current - min_buy
    6. Keep track of max. possible profit
    7. Return the value
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_profit = prices[0], prices[0], float('-infinity')
        for i in prices:
            if i<min_buy:
                min_buy = i
            max_profit = max(max_profit, i-min_buy)
        return max_profit