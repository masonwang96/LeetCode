class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit +=  prices[i+1]-prices[i]
        return profit


if __name__ == "__main__":
    x = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(x))
