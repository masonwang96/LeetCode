class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res = -99999999999999999
        for x in nums:
            sum = max(x, x + sum)
            res = max(res, sum)
        return res


if __name__ == "__main__":
    x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(x))
    assert (Solution().maxSubArray(x) == 6)
