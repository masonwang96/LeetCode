class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [s.index(x) for x in s if s.count(x) == 1]
        return res[0] if res else -1


if __name__ == "__main__":
    x = "leetcode"
    # x = "cc"
    print(Solution().firstUniqChar(x))
