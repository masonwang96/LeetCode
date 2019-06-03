class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # A：65
        s = ''
        while n:
            n -= 1
            s = chr(n % 26 + 65) + s
            n = n // 26
        return s


if __name__ == "__main__":
    x = 28
    print(Solution().convertToTitle(x))
