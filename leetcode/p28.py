'''
@author: adnan
Problem No. 322. Coin Change (Medium)

Runtime: 1312 ms, faster than 34.34% of Python online submissions for Coin Change.
Memory Usage: 12 MB, less than 57.50% of Python online submissions for Coin Change.
'''
class Solution(object):
  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount < 0 or len(coins)==0:
      return -1
    
    dp = [amount+1 for _ in range(amount+1)]
    dp[0] = 0
    for i in range(0,amount+1):
      for j in range(len(coins)):
        if coins[j] <= i:
          dp[i] = min(dp[i], 1 + dp[i-coins[j]])

    if dp[amount] != amount+1:
      return dp[amount]
    else:
      return -1

if __name__ == '__main__':

  sol = Solution()
  testcase, amt = [1, 2, 5], -1
  ans = sol.coinChange(testcase, amt)
  print(f'ans = {ans}')