class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = ''
        first = strs[0]
        others = strs[1:]
        for i in first:
            prefix += i
            for w in others:
                if not w.startswith(prefix):
                    return prefix[:-1]
        return prefix


if __name__ == "__main__":
    x = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(x))
    assert (Solution().longestCommonPrefix(x) == 'fl')
    x = ["dog", "racecar", "car"]
    print(Solution().longestCommonPrefix(x))
    assert (Solution().longestCommonPrefix(x) == '')
