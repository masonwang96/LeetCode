class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))


if __name__ == "__main__":
    x = 5
    print(Solution().isPowerOfTwo(x))
