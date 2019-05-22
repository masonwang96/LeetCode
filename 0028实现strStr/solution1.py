class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == "__main__":
    x = 'hello000'
    y = 'll'
    print(Solution().strStr(x, y))
    assert (Solution().strStr(x, y) == 2)
    x = 'aaaaaa'
    y = 'bba'
    print(Solution().strStr(x, y))
    assert (Solution().strStr(x, y) == -1)
