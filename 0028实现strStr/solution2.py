class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        i, j = 0, 0
        res = -1
        while i < len(haystack):
            if haystack[i] == needle[j]:
                temp = i
                i += 1
                j += 1
            while j < (len(needle)):
                pass




if __name__ == "__main__":
    x = 'hello000'
    y = 'll'
    print(Solution().strStr(x, y))
    assert (Solution().strStr(x, y) == 2)
    x = 'aaaaaa'
    y = 'bba'
    print(Solution().strStr(x, y))
    assert (Solution().strStr(x, y) == -1)
