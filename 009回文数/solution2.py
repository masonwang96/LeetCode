class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        reverse_x = x[::-1]
        if x == reverse_x:
            return True
        return False


if __name__ == "__main__":
    x = 121
    assert (Solution().isPalindrome(x) == True)
    x = 10
    assert (Solution().isPalindrome(x) == False)
