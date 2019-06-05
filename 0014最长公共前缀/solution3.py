class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if not x == s2[i]:
                return s2[:i]
        return s1


if __name__ == "__main__":
    x = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(x))
    assert (Solution().longestCommonPrefix(x) == 'fl')
    x = ["dog", "racecar", "car"]
    print(Solution().longestCommonPrefix(x))
    assert (Solution().longestCommonPrefix(x) == '')
