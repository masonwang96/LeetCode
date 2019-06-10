class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def ispower(x):
            if x == 2 or x == 1:
                return True
            elif x == 3 or x % 2 != 0:
                return False
            else:
                return ispower(x / 2)

        if n < 1:
            return False
        return ispower(n)


if __name__ == "__main__":
    x = 5
    print(Solution().isPowerOfTwo(x))
