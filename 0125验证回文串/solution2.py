class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = s.lower()
        # s = [w for w in s if w.isalpha()]
        # s = ''.join(s)
        # return s == s[::-1]

        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


if __name__ == "__main__":
    x = '0P'
    print(Solution().isPalindrome(x))
