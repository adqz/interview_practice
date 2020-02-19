'''
@author: adnan
Problem 714. Best Time to Buy and Sell Stock with Transaction Fee (Medium)

Runtime: 780 ms, faster than 63.33% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 19.7 MB, less than 12.50% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash_no_stock, cash_stock = 0, -prices[0]
        for stock_price in prices[1:]:
            cash_no_stock = max(cash_no_stock, cash_stock + stock_price - fee)
            cash_stock = max(cash_stock, cash_no_stock - stock_price)
        
        return cash_no_stock

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)) #8