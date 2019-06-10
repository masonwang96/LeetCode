class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num ** 0.5 == int(num ** 0.5):
        #     return True
        # return False
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


if __name__ == "__main__":
    x = 16
    print(Solution().isPerfectSquare(x))
