class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = []
        in_day, out_day = [], []
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit.append(prices[i + 1] - prices[i])
                in_day.append(i)
                out_day.append(i + 1)
        j = 0
        while j < len(out_day) - 1:
            if out_day[j] == in_day[j + 1]:
                out_day.pop(j)
                in_day.pop(j + 1)
                profit[j] += profit[j + 1]
                profit.pop(j + 1)
            j += 1
        profit.sort(reverse=True)
        profit = profit[:2]

        return sum(profit)


if __name__ == "__main__":
    x = [3, 3, 5, 0, 0, 3, 1, 4]
    x = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(Solution().maxProfit(x))
