class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


if __name__ == "__main__":
    x = '()'
    print(Solution().isValid(x))
    assert (Solution().isValid(x) == True)
    x = '()[]{}'
    print(Solution().isValid(x))
    assert (Solution().isValid(x) == True)
    x = '[)'
    print(Solution().isValid(x))
    assert (Solution().isValid(x) == False)
