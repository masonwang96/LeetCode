class Solution(object):
    def maxProfit(self, prices):
        """
        ----------动态规划----------
        呀呀呀呀呀呀呀呀
        ！！！！！！！！！！！！！！！！！！！！
        :type prices: List[int]
        :rtype: int
        """
        # min_price, max_price = 9999999999, 0
        # for i in range(len(prices)):
        #     min_price = min(min_price, prices[i])
        #     max_price = max(max_price, prices[i] - min_price)
        # return max_price

        if not prices:
            return 0
        min_price, max_profits = prices[0], 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            max_profits = max(prices[i] - min_price, max_profits)
        return max_profits

if __name__ == "__main__":
    x = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(x))
