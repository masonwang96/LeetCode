class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = []
        # prices = []
        i = 1
        while i < len(prices) - 1:
            if prices[i - 1] < prices[i] < prices[i + 1] or prices[i - 1] > prices[i] > prices[i + 1]:
                prices.pop(i)
            i += 1

        print('')


if __name__ == "__main__":
    x = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(Solution().maxProfit(x))
