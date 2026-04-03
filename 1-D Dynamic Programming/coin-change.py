'''
* Coin Change: https://leetcode.com/problems/coin-change/description/
'''

from typing import List

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    
        # DP array where finArr[i] stores the minimum coins needed for amount i
        # finArr = [-1 for _ in range(amount + 1)]
        # finArr[0] = 0

        # for i in range(1, amount + 1):
        #     if i in coins:
        #         finArr[i] = 1
        #     else:
        #         for coin in coins:
        #             if coin < i and finArr[i - coin] != -1:
        #                 if finArr[i] == -1:
        #                     finArr[i] = 1 + finArr[i - coin]
        #                 else:
        #                     finArr[i] = min(finArr[i], 1 + finArr[i - coin])

        # return finArr[amount]


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3     # 5+5+1
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    assert s.coinChange([2], 4) == 2
    assert s.coinChange([186,419,83,408], 6249) == 20
    print("All tests passed ✅")
