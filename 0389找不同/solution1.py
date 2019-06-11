class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for x in s:
            t = t.replace(x, '', 1)
        return t


if __name__ == "__main__":
    x = "abcd"
    y = "abcde"
    x = "a"
    y = "aa"
    print(Solution().findTheDifference(x, y))
