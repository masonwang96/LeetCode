class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        half = int(len(x) / 2)
        for i in range(half):
            if not x[i] == x[-i-1]:
                return False
        return True


if __name__ == "__main__":
    x = 121
    assert (Solution().isPalindrome(x) == True)
    x = 10
    assert (Solution().isPalindrome(x) == False)
