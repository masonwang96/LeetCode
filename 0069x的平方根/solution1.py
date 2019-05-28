class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x <= 1:
        #     return x
        i, j = 1, x
        while i <= j:
            mid = (i + j) // 2
            if mid > x / mid:
                j = mid - 1
            elif mid < x / mid:
                i = mid + 1
            else:
                return mid
        return i - 1


if __name__ == "__main__":
    x = 9
    print(Solution().mySqrt(x))
    x = 8
    print(Solution().mySqrt(x))
