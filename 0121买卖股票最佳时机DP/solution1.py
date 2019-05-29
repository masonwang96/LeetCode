class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit


if __name__ == "__main__":
    x = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(x))
