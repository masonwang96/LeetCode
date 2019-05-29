class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, max(prices[i:]) - prices[i])
        return profit


if __name__ == "__main__":
    x = [7, 1, 5, 3, 6, 4]
    # x = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(x))
