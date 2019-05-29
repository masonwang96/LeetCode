class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)):
            temp = [x for x in prices[i:] if x > prices[i]]
            if not temp:
                continue
            profit = max(profit, max(temp) - prices[i])
        return profit


if __name__ == "__main__":
    x = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(x))
