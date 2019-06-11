class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        for key, value in d.items():
            if value == 1:
                return s.index(key)
        return -1


if __name__ == "__main__":
    x = "leetcode"
    # x = "cc"
    print(Solution().firstUniqChar(x))
