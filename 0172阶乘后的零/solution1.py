class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            count += n / 5
            n /= 5

        return count


if __name__ == "__main__":
    x = 4
    print(Solution().trailingZeroes(x))
